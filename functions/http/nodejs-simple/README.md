# Simple Cloud Function to reverse a word

#### Run
    
```bash
npm start
```

#### Test

```bash
curl  http://localhost:8080\?word\="edi"  
```

#### Deploy

```bash
gcloud functions deploy nodejs-word-reverser \
  --region=europe-west3 \
  --runtime=nodejs18  \
  --source=. \
  --entry-point=handler \
  --trigger-http \
  --max-instances=1 \
  --memory=128MB \
  --allow-unauthenticated
```