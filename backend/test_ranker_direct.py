import sys
from ranker import rank_resumes  # your current ranker.py (with CountVectorizer & clean_text)

# Hardcoded job description (exactly as you type in frontend)
job_desc = "Looking for a Python Developer with experience in Flask, REST APIs, and databases. degree in computer science cgpa >3.5"

# Hardcoded resume content (copy-paste of resume01.txt content)
resume01_text = """Name: Alice Chen
Email: alice.chen@example.com
Phone: (555) 123-4567

EDUCATION
M.Sc. in Computer Science, Stanford University, CGPA: 3.9/4.0
B.Sc. in Computer Science, UC Berkeley, CGPA: 3.8/4.0

SKILLS
- Languages: Python, Java, SQL
- Web Frameworks: Flask, Django, FastAPI
- Databases: PostgreSQL, MongoDB, MySQL
- API Design: REST, GraphQL
- Other: Git, Docker, AWS

EXPERIENCE
Backend Python Developer | TechCorp (2022–Present)
- Built RESTful APIs using Flask, handling 10,000+ requests per minute.
- Designed and optimized PostgreSQL database schemas for high‑throughput applications.
- Implemented JWT authentication and rate limiting for public APIs.

Software Engineer | DataWorks (2020–2022)
- Developed Flask‑based microservices for internal data processing pipelines.
- Integrated REST APIs with third‑party services (Stripe, SendGrid).

PROJECTS
- Resume Ranker: Flask app that uses TF‑IDF and cosine similarity to rank resumes.
- E‑commerce API: REST API with Flask, SQLAlchemy, and JWT.

CERTIFICATIONS
- Python Institute PCEP
- AWS Certified Developer – Associate"""

# Hardcoded weak resume (business admin)
resume3_text = """Alex Johnson
alex.j@email.com | (555) 987-6543

PROFILE
Detail-oriented professional with strong communication and problem-solving skills.

EXPERIENCE
Project Coordinator | Business Corp (2019–Present)
- Managed cross-functional teams.

EDUCATION
B.A. in Business Administration | City College (2013–2017)

SKILLS
MS Office, Google Workspace, Basic Python, Team Collaboration"""

resumes_data = [
    {"filename": "resume01.txt", "text": resume01_text},
    {"filename": "resume3.txt", "text": resume3_text}
]

results = rank_resumes(job_desc, resumes_data)
print("Ranking results:")
for r in results:
    print(f"  {r['filename']}: {r['score']}")