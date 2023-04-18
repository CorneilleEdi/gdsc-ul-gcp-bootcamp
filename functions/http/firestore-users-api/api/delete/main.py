import functions_framework
from google.cloud import firestore


@functions_framework.http
def handler(request):
    if request.method != "DELETE":
        return "Method not allowed", 405

    user_id = request.args.get("user_id")
    clean = request.args.get("clean")

    if not user_id:
        if clean == "true":
            try:
                db = firestore.Client()
                users_ref: firestore.CollectionReference = db.collection("users")
                docs = users_ref.stream()
                for doc in docs:
                    doc.reference.delete()
                return {"message": "All users deleted successfully"}
            except Exception as e:
                return f"An Error Occurred: {e}", 500
        return "Invalid request", 400

    try:
        db = firestore.Client()
        users_ref = db.collection("users")
        doc = users_ref.document(user_id).get()
        user = doc.to_dict()
        if not user:
            return f"User {user_id} not found", 404
        doc.reference.delete()
        return {"message": f"User {user_id} deleted successfully"}

    except Exception as e:
        return f"An Error Occurred: {e}", 500
