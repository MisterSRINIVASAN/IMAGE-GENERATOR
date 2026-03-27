import React, { useState } from 'react';
import './Generator.css';

const Generator = ({ onImageGenerated }) => {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;
    
    setLoading(true);
    setError('');
    
    try {
      const response = await fetch('http://127.0.0.1:8000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt, num_images: 1 }),
      });
      
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log('Generated:', data);
      
      // Auto-switch to gallery tab
      if (onImageGenerated) {
        onImageGenerated();
      }
      
      setPrompt('');
    } catch (err) {
      setError(err.message || 'An error occurred during generation.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="generator-container glass-panel fade-enter-active">
      <div className="generator-header">
        <h2>Unleash Your Imagination</h2>
        <p>Describe what you want to see, and Lumina AI will bring it to life.</p>
      </div>
      
      <form onSubmit={handleGenerate} className="generator-form">
        <div className="input-group">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="A futuristic city with flying cars at sunset, cinematic lighting, 8k resolution..."
            rows={5}
            className="prompt-input"
            disabled={loading}
          />
        </div>
        
        {error && <div className="error-message">{error}</div>}
        
        <button 
          type="submit" 
          className="btn btn-primary generate-btn"
          disabled={loading || !prompt.trim()}
        >
          {loading ? (
            <>
              <span className="spinner"></span>
              Generating...
            </>
          ) : (
            '✨ Generate Masterpiece'
          )}
        </button>
      </form>
      
      <div className="features-grid">
        <div className="feature-card">
          <div className="feature-icon">🚀</div>
          <h3>GPU Powered</h3>
          <p>Accelerated with CUDA PyTorch support</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">🧠</div>
          <h3>Stable Diffusion</h3>
          <p>CompVis/stable-diffusion-v1-4 Model</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">💾</div>
          <h3>Auto Save</h3>
          <p>Full history tracking in local database</p>
        </div>
      </div>
    </div>
  );
};

export default Generator;
