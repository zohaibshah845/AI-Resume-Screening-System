# backend/text_extractor.py
import PyPDF2
import docx
import os

def extract_text(filepath):
    """Extract text from PDF, DOCX, or TXT file."""
    if not os.path.exists(filepath):
        return ""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.pdf':
        return extract_from_pdf(filepath)
    elif ext == '.docx':
        return extract_from_docx(filepath)
    elif ext == '.txt':
        return extract_from_txt(filepath)
    else:
        return ""

def extract_from_pdf(filepath):
    text = ""
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
    return text

def extract_from_docx(filepath):
    text = ""
    try:
        doc = docx.Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
    return text

def extract_from_txt(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading TXT {filepath}: {e}")
        return ""