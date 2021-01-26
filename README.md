## Thank you for reviewing

---

1. Clone this repository
   
2. Create `env` file in the project directory from `env.example`
```json
AWS_DEFAULT_REGION=us-east-1
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
PUMP_INTERVAL=2
WEBHOOK_URL=https://webhook.site/xxx
```
Please input the exact information.

3. Build Docker image
> docker image build -t <name of container> .

4. Run Docker image
>docker run -it --env-file=env <name of container>
