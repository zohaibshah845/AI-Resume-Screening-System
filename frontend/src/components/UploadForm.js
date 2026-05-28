import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { uploadResumes } from '../services/api';   // import API from services

const UploadForm = ({ onResults }) => {
  const [jobDescription, setJobDescription] = useState('');
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!jobDescription.trim()) {
      alert('Please enter a job description');
      return;
    }
    if (resumes.length === 0) {
      alert('Please select at least one resume file');
      return;
    }

    const formData = new FormData();
    formData.append('job_description', jobDescription);
    for (let i = 0; i < resumes.length; i++) {
      formData.append('resumes', resumes[i]);
    }

    setLoading(true);
    try {
      const response = await uploadResumes(formData);
      onResults(response.data);
    } catch (error) {
      console.error('Upload error:', error);
      alert('Failed to screen resumes. Check backend.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3">
        <Form.Label>Job Description (paste text here)</Form.Label>
        <Form.Control
          as="textarea"
          rows={6}
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          placeholder="Paste the job description here..."
          required
        />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Resumes (PDF, DOCX, TXT – multiple allowed)</Form.Label>
        <Form.Control
          type="file"
          multiple
          accept=".pdf,.docx,.txt"
          onChange={(e) => setResumes([...e.target.files])}
          required
        />
      </Form.Group>

      <Button variant="primary" type="submit" disabled={loading}>
        {loading ? 'Screening...' : 'Screen Resumes'}
      </Button>
    </Form>
  );
};

export default UploadForm;   // ✅ Default export of the component