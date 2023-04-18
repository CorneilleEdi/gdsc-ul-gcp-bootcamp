# Cloud Workflows Sample

This is simple sample that demonstrates how to use Cloud Workflows to generate random numbers by calling a Cloud
Function.

## Create workflow

```bash 
gcloud workflows deploy number-generator --source=workflow.yaml --location=europe-west3
```

## Run workflow

```bash
gcloud workflows execute number-generator --location=europe-west3
```
