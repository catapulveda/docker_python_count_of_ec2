import os
import json
import time
import boto3
import requests
from datetime import datetime

def get_count_ec2():
    try:
        ec2 = boto3.resource('ec2')
        # Boto3
        # Use the filter() method of the instances collection to retrieve
        # all running EC2 instances.
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for ec2_count, instance in enumerate(instances, start=1):
            print(instance.id, instance.instance_type)
        return int(ec2_count)
    except Exception as e:
        print(e)

def invoke_webhook(payload):
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url=os.environ['WEBHOOK_URL'], headers=headers, data=json.dumps(payload))
        if r.status_code == 200:
            print(f"Success on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Failed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        ec2_count = get_count_ec2()
        payload = {
            "ec2_count": ec2_count,
            "checked_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        invoke_webhook(payload)

        time.sleep(int(os.environ['PUMP_INTERVAL'])*60)

