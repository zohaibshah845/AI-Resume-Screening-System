import re

def clean_and_tokenize(text):
    """Lowercase, remove punctuation, split into words, remove common stop words."""
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    # Split into words
    words = text.split()
    # Simple stop words (you can add more)
    stop_words = {'the', 'a', 'an', 'and', 'of', 'to', 'in', 'for', 'on', 'with', 'by', 'is', 'are', 'at', 'from', 'as', 'be', 'this', 'that', 'was', 'were', 'has', 'have', 'had'}
    words = [w for w in words if w not in stop_words and len(w) > 2]
    return set(words)

def rank_resumes(job_description, resumes_text):
    """
    Returns scores from 0-100 based on the percentage of job description keywords
    that appear in each resume (case‑insensitive, ignoring punctuation).
    """
    job_keywords = clean_and_tokenize(job_description)
    if not job_keywords:
        return [{'filename': r['filename'], 'score': 0} for r in resumes_text]

    results = []
    for r in resumes_text:
        resume_keywords = clean_and_tokenize(r['text'])
        # Count how many job keywords appear in the resume
        matched = len(job_keywords & resume_keywords)
        score = int(round((matched / len(job_keywords)) * 100))
        results.append({'filename': r['filename'], 'score': score})

    results.sort(key=lambda x: x['score'], reverse=True)
    return results