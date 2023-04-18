import uuid

import functions_framework
from google.cloud import firestore


@functions_framework.http
def handler(request):
    if request.method != "POST":
        return "Method not allowed", 405

    data = request.get_json()
    if not data:
        return "Invalid request", 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return "Invalid request data", 400

    user_id = str(uuid.uuid4())
    try:

        db = firestore.Client()
        doc_ref = db.collection("users").document(user_id)
        doc_ref.set({"name": name, "email": email, "uuid": user_id})
    except Exception as e:
        return f"An Error Occurred: {e}", 500

    return {"message": f"User {user_id} added successfully"}
