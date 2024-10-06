import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Output from './pages/Output';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/output" element={<Output />} />
        {/* You can add more routes here for additional pages */}
      </Routes>
    </Router>
  )
}

export default App
