
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Replace with your Firebase service account key path
# Download it from Firebase Console -> Project Settings -> Service Accounts
# Correct (actual file name in the same folder)
cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_screening_result(job_filename, results):
    """Save a screening session to Firestore."""
    doc_ref = db.collection('screening_results').document()
    doc_ref.set({
        'job_filename': job_filename,
        'timestamp': firestore.SERVER_TIMESTAMP,
        'results': results   # list of {'filename': ..., 'score': ...}
    })
    return doc_ref.id