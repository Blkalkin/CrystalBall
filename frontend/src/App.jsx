import './App.css'
import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Output from './pages/Output';
import Output1 from './pages/Output1';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/output" element={<Output />} />
        <Route path="/output1" element={<Output1 />} />
        {/* You can add more routes here for additional pages */}
      </Routes>
    </Router>
  )
}

export default App
