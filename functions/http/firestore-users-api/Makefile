# Specify ports for all functions to run on
GET_PORT = 5001
POST_PORT = 5002
UPDATE_PORT = 5003
DELETE_PORT = 5004

# Create command to print help
help:
	@echo "Makefile for Firestore Users API"
	@echo "Usage:"
	@echo "  make run - Run all functions get, post, update and delete locally on ports $(GET_PORT), $(POST_PORT), $(UPDATE_PORT) and $(DELETE_PORT)"
	@echo "  make deploy-get - Deploy get function to Cloud Functions"
	@echo "  make deploy-post - Deploy post function to Cloud Functions"
	@echo "  make deploy-update - Deploy update function to Cloud Functions"
	@echo "  make deploy-delete - Deploy delete function to Cloud Functions"
	@echo "  make deploy-all - Deploy all functions to Cloud Functions"
	@echo "  make get - Run get function locally on port $(GET_PORT)"
	@echo "  make post - Run post function locally on port $(POST_PORT)"
	@echo "  make update - Run update function locally on port $(UPDATE_PORT)"
	@echo "  make delete - Run delete function locally on port $(DELETE_PORT)"

# Create run commands for each function
get:
	@echo "Running get function..."
	cd api/get && functions-framework --target=handler --port=$(GET_PORT) --debug

post:
	@echo "Running post function..."
	cd api/post && functions-framework --target=handler --port=$(POST_PORT) --debug

update:
	@echo "Running update function..."
	cd api/update && functions-framework --target=handler --port=$(UPDATE_PORT) --debug

delete:
	@echo "Running delete function..."
	cd api/delete && functions-framework --target=handler --port=$(DELETE_PORT) --debug

# Create a command to run all functions
run:
	@echo "Running all functions..."
	$(MAKE) get
	$(MAKE) post
	$(MAKE) update
	$(MAKE) delete


# Create a command to deploy a single function
deploy-get:
	@echo "Deploying get function..."
	cd api/get && gcloud functions deploy firestore-users-api-get --runtime python310 --entry-point=handler  --region=europe-west3 --max-instances=1 --trigger-http --allow-unauthenticated

deploy-post:
	@echo "Deploying post function..."
	cd api/post && gcloud functions deploy firestore-users-api-post --runtime python310 --entry-point=handler  --region=europe-west3 --max-instances=1 --trigger-http --allow-unauthenticated

deploy-update:
	@echo "Deploying update function..."
	cd api/update && gcloud functions deploy firestore-users-api-update --runtime python310 --entry-point=handler  --region=europe-west3 --max-instances=1 --trigger-http --allow-unauthenticated

deploy-delete:
	@echo "Deploying delete function..."
	cd api/delete && gcloud functions deploy firestore-users-api-delete --runtime python310 --entry-point=handler  --region=europe-west3 --max-instances=1 --trigger-http --allow-unauthenticated


# Create a command to deploy all functions
deploy-all:
	@echo "Deploying all functions..."
	$(MAKE) deploy-get
	$(MAKE) deploy-post
	$(MAKE) deploy-update
	$(MAKE) deploy-delete

