# API for users with Firestore, Cloud Functions and API Gateway

#### Create API

```bash
gcloud api-gateway apis create firestore-users-api --project=gdsc-ul-playground-eros
```

#### Create API Config

```bash
gcloud api-gateway api-configs create firestore-users-api-config \
  --api=firestore-users-api \
  --project=gdsc-ul-playground-eros \
  --openapi-spec=open-api.yaml
```

#### Delete API Config

```bash
gcloud api-gateway api-configs delete firestore-users-api-config \
  --api=firestore-users-api \
  --project=gdsc-ul-playground-eros
```

#### Create Gateway

```bash
gcloud api-gateway gateways create firestore-users-api-gateway \
  --api=firestore-users-api \
  --api-config=firestore-users-api-config \
  --location=europe-central1 \
  --project=gdsc-ul-playground-eros
```

#### Delete Gateway

```bash
gcloud api-gateway gateways delete firestore-users-api-gateway \
  --location=europe-central1 \
  --project=gdsc-ul-playground-eros
```
