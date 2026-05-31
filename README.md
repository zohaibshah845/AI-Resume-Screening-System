
AI Resume Screener — 
an AI-powered resume ranking system using TF‑IDF and cosine similarity. Upload a job description + multiple resumes, the system extracts text, preprocesses, and ranks candidates by semantic match. Built with React, Flask, and Firebase.



Key features
. Upload job description (PDF/DOCX/TXT)
. Upload multiple resumes
. Automatic text extraction and preprocessing (tokenization, stopword removal)
. Ranking using TF‑IDF vectorization + cosine similarity
. Ranked results displayed in a clear table with similarity scores
. File validation and temporary storage (auto‑cleanup)
. Firebase Firestore integration for screening history

Tech stack
. Frontend: React, Bootstrap, Axios
. Backend: Python, Flask
. NLP / ML: scikit-learn (TF‑IDF), NLTK, cosine similarity
. File parsing: PyPDF2, pdfplumber, python-docx
. Database: Firebase Firestore
. Auth: (optional) JWT / Firebase Auth ready

Project structure

AI-Resume-Screener/
├── backend/
│   ├── app.py
│   ├── text_extractor.py
│   ├── preprocessor.py
│   ├── ranker.py
│   ├── firebase_client.py
│   ├── requirements.txt
│   └── uploads/            (temporary – auto-cleaned)
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
. Node.js (v18+)
. npm (v9+)
. Python (3.8+)
. Firebase account (optional)

Environment variables
Create a .env file in backend/ (optional, for Firebase):
  FIREBASE_CREDENTIALS_PATH=firebase-adminsdk.json
Do not commit the actual firebase-adminsdk.json file. Add it to .gitignore.

Quick start

Backend (Flask API)
  cd backend
  pip install -r requirements.txt
  python -m nltk.downloader punkt stopwords
  python app.py
Server runs at http://localhost:5000

Frontend (React client)
  cd frontend
  npm install
  npm start
Client opens at http://localhost:3000

How to use
. Open http://localhost:3000
. Upload a job description file (PDF/DOCX/TXT)
. Upload one or more resume files (same formats)
. Click Screen Resumes
. View ranked results – higher score = better match

Testing notes
. Manual test cases:
  - Upload valid/invalid file types → validation works
  - No file selected → error message
  - Different resume contents → scores reflect similarity
  - Backend returns JSON with ranked_resumes array
. Firebase storage can be verified by checking Firestore collection screening_results

Troubleshooting
. Backend won't start: check port 5000 is free and dependencies installed (pip list)
. Text extraction fails: confirm the uploaded file is not corrupted and is PDF/DOCX/TXT
. No ranking results: ensure job description and resumes contain enough text (at least a few sentences)
. Firestore save fails: system still returns results – check firebase-adminsdk.json path and network

Author
Syed Zohaib (F22BSEEN1E02046)
Software Engineering, IUB
Supervisor: Mam Alisha fida

Deliverables
. SRS & SDD (Google Drive folder link)
. Demo video (YouTube unlisted link)
. GitHub repository (this one)


