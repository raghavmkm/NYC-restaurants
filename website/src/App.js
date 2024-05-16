import React, { useState } from 'react';
import Hello from './Hello';
import './App.css';
import exampleImage1 from './image1.jpg';
import exampleImage2 from './image2.jpg';
import exampleImage3 from './image3.jpg';
import exampleImage4 from './image4.jpg';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/compute', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: inputValue }),
    });
    const data = await response.json();
    setResult(data.result);
  };

  return (
    <div className="App">
      <Hello/>
      <img src={exampleImage1} alt="Example" />
      <img src={exampleImage2} alt="Example" />
      <img src={exampleImage3} alt="Example" />
      <img src={exampleImage4} alt="Example" />
      <h4>Enter the name of a restaurant you ejoyed...</h4>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      <h4>Similar restaurants you may enjoy are:</h4>
      {result && <p>{result}</p>}
    </div>
  );
}

export default App;
