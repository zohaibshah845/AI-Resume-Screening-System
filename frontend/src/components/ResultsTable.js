import React from 'react';
import { Table } from 'react-bootstrap';

const ResultsTable = ({ results }) => {
  if (!results || results.length === 0) {
    return <p className="mt-3">No results to display.</p>;
  }

  return (
    <Table striped bordered hover className="mt-4">
      <thead>
        <tr>
          <th>Rank</th>
          <th>Resume Filename</th>
          <th>Similarity Score</th>
        </tr>
      </thead>
      <tbody>
        {results.map((item, idx) => (
          <tr key={idx}>
            <td>{idx + 1}</td>
            <td>{item.filename}</td>
            <td>{item.score}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default ResultsTable;