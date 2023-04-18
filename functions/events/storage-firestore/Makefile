# Variables definition
PROJECT_ID=gdsc-ul-playground-eros
COLLECTION_NAME=storage-files
BUCKET_NAME=gs://fire-event-$(PROJECT_ID)

help:
	@echo "make make-bucket - Create a bucket"
	@echo "make deploy-upload - Deploy the Cloud Function storage-firestore-upload"
	@echo "make deploy-delete - Deploy the Cloud Function storage-firestore-delete"

make-bucket:
	@echo "Creating bucket $(BUCKET_NAME)"
	gsutil mb $(BUCKET_NAME)

# Script to deploy the Cloud Function
deploy-upload:
	@echo "Deploying Cloud Function storage-firestore-upload"
	cd upload && gcloud functions deploy storage-firestore-upload \
	--runtime python310 \
	--entry-point=upload_event_handler \
	--region=europe-west3 \
	--max-instances=1 \
	--trigger-resource $(BUCKET_NAME) \
	--trigger-event google.storage.object.finalize \
	--set-env-vars BUCKET_NAME=$(BUCKET_NAME),COLLECTION_NAME=$(COLLECTION_NAME)


deploy-delete:
	@echo "Deploying Cloud Function storage-firestore-delete"
	cd delete && gcloud functions deploy storage-firestore-delete \
	--runtime python310 \
	--entry-point=delete_event_handler \
	--region=europe-west3 \
	--max-instances=1 \
	--trigger-resource $(BUCKET_NAME) \
	--trigger-event google.storage.object.delete \
	--set-env-vars BUCKET_NAME=$(BUCKET_NAME),COLLECTION_NAME=$(COLLECTION_NAME)