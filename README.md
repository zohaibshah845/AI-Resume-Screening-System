AI Resume Screener — an AI-powered resume ranking system (React + Flask + Firebase) that uses TF‑IDF and cosine similarity to match multiple resumes against a job description.

Key features
. User uploads a job description (PDF/DOCX/TXT) and multiple resumes
. Automatic text extraction and preprocessing (tokenization, stopword removal)
. Ranking using TF‑IDF vectorization + cosine similarity
. Ranked results displayed in a clear table with similarity scores
. File validation & temporary storage (auto‑cleanup)
. Firebase Firestore integration to log screening history

Tech stack
. Frontend: React, Bootstrap, Axios
. Backend: Python, Flask
. NLP / ML: scikit-learn (TF‑IDF), NLTK, cosine similarity
. File parsing: PyPDF2, pdfplumber, python-docx
. Database: Firebase Firestore
. Auth: (optional) JWT / Firebase Auth ready

Project structure (important folders)

AI-Resume-Screener/
├── backend/
│   ├── app.py
│   ├── text_extractor.py
│   ├── preprocessor.py
│   ├── ranker.py
│   ├── firebase_client.py
│   ├── requirements.txt
│   └── uploads/            (temporary – auto‑cleaned)
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.js
│   ├── package.json
│   └── package-lock.json
├── README.md
└── .gitignore

Prerequisites
. Node.js (v18+ recommended)
. npm (v9+)
. Python (3.8+)
. (Optional) Firebase account for Firestore logging

Environment variables
Create a `.env` file in `backend/` (optional – only for Firebase):
. FIREBASE_CREDENTIALS_PATH=firebase-adminsdk.json
. Do **not** commit the actual `firebase-adminsdk.json` file. Put it in `.gitignore`.

Quick start

Backend (Flask API)
. cd backend
. pip install -r requirements.txt
. python -m nltk.downloader punkt stopwords
. python app.py
Server runs at `http://localhost:5000`

Frontend (React client)
. cd frontend
. npm install
. npm start
Client opens at `http://localhost:3000`

How to use
. 1. Open the React app.
. 2. Upload a job description file (PDF/DOCX/TXT).
. 3. Upload one or more resume files (same formats).
. 4. Click **Screen Resumes**.
. 5. View the ranked table – resumes with higher similarity scores are better matches.

Testing notes
. Manual test cases:
.   - Upload valid/invalid file types → validation works.
.   - No file selected → error message.
.   - Different resume contents → scores reflect similarity.
.   - Backend returns JSON with `ranked_resumes` array.
. Firebase storage can be verified by checking Firestore collection `screening_results`.

How to contribute
. Fork the repo
. Create a branch for your feature
. Commit and open a PR

Troubleshooting
. **Backend won't start:** Check that all dependencies are installed (`pip list`) and port 5000 is free.
. **Text extraction fails:** Ensure the uploaded file is not corrupted and is a supported format.
. **No ranking results:** Verify that the job description and resumes contain enough text (at least a few sentences).
. **Firestore save fails:** The system still returns results – check your `firebase-adminsdk.json` path and network.

Author
Syed Zohaib (F22BSEEN1E02046)
Software Engineering, IUB
Supervisor: Mam Alishba  Fida

Deliverables
. SRS & SDD (Google Drive folder)
. Demo video (YouTube, unlisted)
. GitHub repository (this one)
