AI Resume Screener — an AI-powered resume ranking system using TF‑IDF and cosine similarity.

Key features
. Upload job description (PDF/DOCX/TXT)
. Upload multiple resumes
. Text extraction and preprocessing
. Rank resumes by similarity score
. File validation and temporary storage
. Firebase Firestore for screening history

Tech stack
. Frontend: React, Bootstrap
. Backend: Python, Flask
. NLP: scikit-learn, NLTK, cosine similarity
. File parsing: PyPDF2, pdfplumber, python-docx
. Database: Firebase Firestore

Project structure
AI-Resume-Screener/
  backend/
    app.py
    text_extractor.py
    preprocessor.py
    ranker.py
    firebase_client.py
    requirements.txt
  frontend/
    public/
    src/
    package.json
  README.md
  .gitignore

Prerequisites
. Node.js (v18+)
. npm (v9+)
. Python (3.8+)
. Firebase account (optional)

Quick start
Backend
. cd backend
. pip install -r requirements.txt
. python -m nltk.downloader punkt stopwords
. python app.py

Frontend
. cd frontend
. npm install
. npm start

How to use
. Open http://localhost:3000
. Upload job description file
. Upload one or more resumes
. Click Screen Resumes
. View ranked results with similarity scores

Troubleshooting
. Backend won't start: check port 5000 is free and dependencies installed
. Text extraction fails: check file is not corrupted
. No ranking results: ensure text content exists in files

Author
Muhammad Rashid (F22BSEEN1E02051)
IUB, Supervisor: Ms Tayyaba Rashid

Deliverables
. SRS & SDD (Google Drive)
. Demo video (YouTube unlisted)
. GitHub repository
