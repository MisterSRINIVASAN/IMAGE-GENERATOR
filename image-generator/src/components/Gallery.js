import React, { useState, useEffect } from 'react';
import './Gallery.css';

const Gallery = () => {
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);

  const fetchImages = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/images');
      if (!response.ok) throw new Error('Failed to fetch images');
      const data = await response.json();
      setImages(data);
    } catch (err) {
      setError('Could not load your image history.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchImages();
  }, []);

  const handleDelete = async (id, e) => {
    e.stopPropagation(); // Prevent opening modal
    if (!window.confirm('Are you sure you want to delete this image?')) return;
    
    try {
      const response = await fetch(`http://127.0.0.1:8000/images/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Failed to delete');
      
      // Remove from state
      setImages(images.filter(img => img.id !== id));
      if (selectedImage && selectedImage.id === id) {
        setSelectedImage(null);
      }
    } catch (err) {
      alert('Error deleting image: ' + err.message);
    }
  };

  const toggleFavorite = async (image, e) => {
    e.stopPropagation();
    try {
      const response = await fetch(`http://127.0.0.1:8000/images/${image.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_favorite: !image.is_favorite }),
      });
      
      if (!response.ok) throw new Error('Failed to update');
      
      // Update state
      setImages(images.map(img => 
        img.id === image.id ? { ...img, is_favorite: !img.is_favorite } : img
      ));
      
      if (selectedImage && selectedImage.id === image.id) {
        setSelectedImage({ ...selectedImage, is_favorite: !image.is_favorite });
      }
    } catch (err) {
      alert('Error updating image: ' + err.message);
    }
  };

  if (loading) {
    return (
      <div className="gallery-loading">
        <div className="spinner pulse" style={{ width: '40px', height: '40px' }}></div>
        <p>Loading your masterpieces...</p>
      </div>
    );
  }

  return (
    <div className="gallery-container fade-enter-active">
      {error && <div className="error-message">{error}</div>}
      
      {images.length === 0 && !error ? (
        <div className="empty-state glass-panel">
          <h3>No images yet</h3>
          <p>Head over to the Generate workspace to create your first image.</p>
        </div>
      ) : (
        <div className="image-grid">
          {images.map(image => (
            <div key={image.id} className="image-card" onClick={() => setSelectedImage(image)}>
              <div className="image-wrapper">
                <img 
                  src={`http://127.0.0.1:8000/images_static/${image.file_path.split('\\').pop().split('/').pop()}`} 
                  alt={image.prompt} 
                  loading="lazy"
                />
                <div className="image-overlay">
                  <p className="prompt-text line-clamp">{image.prompt}</p>
                  <div className="image-actions">
                    <button 
                      className={`action-btn ${image.is_favorite ? 'favorite-active' : ''}`}
                      onClick={(e) => toggleFavorite(image, e)}
                      title="Favorite"
                    >
                      {image.is_favorite ? '❤️' : '🤍'}
                    </button>
                    <button 
                      className="action-btn delete-btn"
                      onClick={(e) => handleDelete(image.id, e)}
                      title="Delete"
                    >
                      🗑️
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Modal for viewing image */}
      {selectedImage && (
        <div className="modal-overlay fade-enter-active" onClick={() => setSelectedImage(null)}>
          <div className="modal-content glass-panel" onClick={e => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setSelectedImage(null)}>✕</button>
            <div className="modal-image-container">
              <img 
                src={`http://127.0.0.1:8000/images_static/${selectedImage.file_path.split('\\').pop().split('/').pop()}`} 
                alt={selectedImage.prompt} 
              />
            </div>
            <div className="modal-details">
              <h3>Prompt</h3>
              <p className="modal-prompt">{selectedImage.prompt}</p>
              <div className="modal-meta">
                <span>Created: {new Date(selectedImage.created_at).toLocaleString()}</span>
                <div className="modal-actions">
                  <button 
                    className={`btn ${selectedImage.is_favorite ? 'btn-primary' : ''}`}
                    onClick={(e) => toggleFavorite(selectedImage, e)}
                  >
                    {selectedImage.is_favorite ? '❤️ Favorited' : '🤍 Add to Favorites'}
                  </button>
                  <button className="btn btn-danger" onClick={(e) => {
                    handleDelete(selectedImage.id, e);
                  }}>
                    🗑️ Delete Image
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Gallery;
