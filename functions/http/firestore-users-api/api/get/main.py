import functions_framework
from google.cloud import firestore


@functions_framework.http
def handler(request):
    if request.method != "GET":
        return "Method not allowed", 405

    user_id = request.args.get("user_id")

    if not user_id:
        try:
            db = firestore.Client()
            users_ref: firestore.CollectionReference = db.collection("users")
            docs = users_ref.limit(20).stream()
            users = []
            for doc in docs:
                users.append(doc.to_dict())
            return {"users": users}

        except Exception as e:
            return f"An Error Occurred: {e}", 500
    else:
        try:
            db = firestore.Client()
            users_ref = db.collection("users")
            doc = users_ref.document(user_id).get()
            user = doc.to_dict()
            if not user:
                return f"User {user_id} not found", 404
            return user

        except Exception as e:
            return f"An Error Occurred: {e}", 500
