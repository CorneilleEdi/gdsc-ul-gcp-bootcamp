import uuid

import functions_framework
from google.cloud import firestore


@functions_framework.http
def handler(request):
    if request.method != "PATCH":
        return "Method not allowed", 405

    user_id = request.args.get("user_id")
    if not user_id:
        return "Invalid request", 400

    data = request.get_json()
    if not data:
        return "Invalid request", 400

    name = data.get("name")
    email = data.get("email")

    if not name and not email:
        return "Invalid request data", 400

    try:
        db = firestore.Client()
        doc_ref = db.collection("users").document(user_id)
        doc = doc_ref.get()
        user = doc.to_dict()
        if not user:
            return f"User {user_id} not found", 404
        if name:
            doc_ref.update({"name": name})
        if email:
            doc_ref.update({"email": email})

        user = doc_ref.get().to_dict()
        return {"message": f"User {user_id} updated successfully", "user": user}
    except Exception as e:
        return f"An Error Occurred: {e}", 500
