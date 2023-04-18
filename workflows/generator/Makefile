# Create a simple workflow that runs a single task
create:
	@echo "Creating workflow..."
	gcloud workflows deploy number-generator --source=workflow.yaml --location=europe-west3

run:
	@echo "Running workflow..."
	gcloud workflows execute number-generator --location=europe-west3
