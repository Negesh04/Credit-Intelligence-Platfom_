import React from 'react';

export default function ScoreDetails({ financials, explanation }) {
  return (
    <div>
      <h3>Financial Indicators</h3>
      <ul>
        {Object.entries(financials).map(([key, value]) => (
          <li key={key}><strong>{key}:</strong> {value}</li>
        ))}
      </ul>
      <h3>Explanation</h3>
      <ul>
        {explanation.map((e, i) => <li key={i}>{e}</li>)}
      </ul>
    </div>
  );
}
