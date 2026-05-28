from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    print("Received request")
    job_desc = request.form.get('job_description', '')
    files = request.files.getlist('resumes')
    results = [{'filename': f.filename, 'score': 100} for f in files]
    return jsonify(results)

@app.route('/')
def home():
    return "OK"

if __name__ == '__main__':from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from text_extractor import extract_text
from ranker import rank_resumes

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        job_desc = request.form.get('job_description', '').strip()
        if not job_desc:
            return jsonify({'error': 'Missing job description'}), 400

        files = request.files.getlist('resumes')
        if not files or files[0].filename == '':
            return jsonify({'error': 'No resumes uploaded'}), 400

        resumes_data = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                text = extract_text(filepath)
                if not text.strip():
                    text = " "
                resumes_data.append({'filename': filename, 'text': text})

        ranked = rank_resumes(job_desc, resumes_data)
        return jsonify(ranked), 200

    except Exception as e:
        print("❌ Backend error:", e)
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return "AI Resume Screener API running", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    app.run(debug=True, port=5000)