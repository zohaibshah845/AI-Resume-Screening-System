import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import UploadForm from './components/UploadForm';
import ResultsTable from './components/ResultsTable';

function App() {
  const [results, setResults] = useState([]);

  return (
    <Container className="mt-5">
      <Row>
        <Col>
          <h1 className="text-center mb-4">AI Resume Screener</h1>
          <UploadForm onResults={setResults} />
          <ResultsTable results={results} />
        </Col>
      </Row>
    </Container>
  );
}

export default App;