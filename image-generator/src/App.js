import React, { useState } from 'react';
import './App.css';
import Generator from './components/Generator';
import Gallery from './components/Gallery';

function App() {
  const [activeTab, setActiveTab] = useState('generate');

  return (
    <div className="App">
      <header className="app-header">
        <h1 className="app-title">Lumina AI</h1>
        <p className="app-subtitle">Create stunning visualizations powered by Stable Diffusion</p>
      </header>

      <div className="tabs">
        <button 
          className={`tab-btn ${activeTab === 'generate' ? 'active' : ''}`}
          onClick={() => setActiveTab('generate')}
        >
          ✨ Generate Workspace
        </button>
        <button 
          className={`tab-btn ${activeTab === 'gallery' ? 'active' : ''}`}
          onClick={() => setActiveTab('gallery')}
        >
          🖼️ Image History
        </button>
      </div>

      <main className="main-content">
        {activeTab === 'generate' && <Generator onImageGenerated={() => setActiveTab('gallery')} />}
        {activeTab === 'gallery' && <Gallery />}
      </main>
    </div>
  );
}

export default App;
