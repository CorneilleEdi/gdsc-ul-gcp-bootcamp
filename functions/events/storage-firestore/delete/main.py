import functions_framework
import os
from google.cloud import firestore

BUCKET_NAME = os.environ.get("BUCKET_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")


@functions_framework.cloud_event
def delete_event_handler(cloud_event):
    print(f"Received event with ID: {cloud_event['id']} and data {cloud_event.data}")

    # {'bucket': 'fire-event-gdsc-ul-playground-eros', 'contentType': 'application/json', 'crc32c': 'dk29dg==', 'etag': 'CNy37qH1s/4CEAE=', 'generation': '1681837591862236', 'id': 'fire-event-gdsc-ul-playground-eros/message_feedback.json/1681837591862236', 'kind': 'storage#object', 'md5Hash': '11FxOYiYfpMxmANj4kGJzg==', 'mediaLink': 'https://storage.googleapis.com/download/storage/v1/b/fire-event-gdsc-ul-playground-eros/o/message_feedback.json?generation=1681837591862236&alt=media', 'metageneration': '1', 'name': 'message_feedback.json', 'selfLink': 'https://www.googleapis.com/storage/v1/b/fire-event-gdsc-ul-playground-eros/o/message_feedback.json', 'size': '2', 'storageClass': 'STANDARD', 'timeCreated': '2023-04-18T17:06:31.996Z', 'timeStorageClassUpdated': '2023-04-18T17:06:31.996Z', 'updated': '2023-04-18T17:06:31.996Z'}
    file_name = cloud_event.data['name'].split('/')[-1]

    db = firestore.Client()
    collection_ref = db.collection(COLLECTION_NAME)
    docu_ref = collection_ref.document(file_name)
    docu_ref.delete()

    return {"message": f"File {file_name} deleted successfully"}
