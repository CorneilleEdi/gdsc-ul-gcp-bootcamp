# Sample Cloud run app

This sample shows how to deploy a simple Cloud Run app.

## Build
    
```bash
export GOOGLE_CLOUD_PROJECT=gdsc-ul-playground-eros
export SERVICE_NAME=hello-world-sample
export VERSION=1.2.0
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/${SERVICE_NAME}:${VERSION}
```

## Deploy

```bash
export GOOGLE_CLOUD_PROJECT=gdsc-ul-playground-eros
export SERVICE_NAME=hello-world-sample
export VERSION=1.2.0
gcloud run deploy ${SERVICE_NAME} --image gcr.io/${GOOGLE_CLOUD_PROJECT}/${SERVICE_NAME}:${VERSION} --platform managed --region europe-west3 --allow-unauthenticated --set-env-vars MESSAGE="Google Cloud Bootcamp" --min-instances 0 --max-instances 2
```
