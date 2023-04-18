# Simple Cloud Function to generate random numbers


#### Run
    
```bash
functions-framework --target=handler --port=8080 --debug
```

#### Test

```bash
curl  http://localhost:8080\?times\=10
```

#### Deploy

```bash
gcloud functions deploy python-random-generator \
  --region=europe-west3 \
  --runtime=python310  \
  --source=. \
  --entry-point=handler \
  --trigger-http \
  --max-instances=1 \
  --allow-unauthenticated
```