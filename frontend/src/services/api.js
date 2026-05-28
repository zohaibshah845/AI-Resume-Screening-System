import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000',  // Make sure this is correct
});

export const uploadResumes = (formData) => {
  return API.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};