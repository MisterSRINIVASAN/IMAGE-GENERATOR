from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
import os

from database import engine, Base, get_db
import models, schemas
from generator import generate_image

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Image Generator API")

# Configure CORS for React frontend (which typically runs on port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the generated images folder
if not os.path.exists("generated_images"):
    os.makedirs("generated_images")
app.mount("/images_static", StaticFiles(directory="generated_images"), name="images_static")

@app.post("/generate", response_model=schemas.ImageResponse)
def create_generation(request: schemas.ImageCreate, db: Session = Depends(get_db)):
    """Generate a new image and store the record in DB"""
    try:
        # Generate the image
        file_path = generate_image(request.prompt)
        
        # Save to database
        db_image = models.ImageRecord(
            prompt=request.prompt,
            file_path=file_path
        )
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/images", response_model=List[schemas.ImageResponse])
def get_images(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    """Retrieve all generated images"""
    images = db.query(models.ImageRecord).order_by(models.ImageRecord.created_at.desc()).offset(skip).limit(limit).all()
    return images

@app.get("/images/{image_id}", response_model=schemas.ImageResponse)
def get_image(image_id: int, db: Session = Depends(get_db)):
    """Get a specific image by ID"""
    db_image = db.query(models.ImageRecord).filter(models.ImageRecord.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@app.put("/images/{image_id}", response_model=schemas.ImageResponse)
def update_image(image_id: int, request: schemas.ImageUpdate, db: Session = Depends(get_db)):
    """Update properties like `is_favorite`"""
    db_image = db.query(models.ImageRecord).filter(models.ImageRecord.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    if request.is_favorite is not None:
        db_image.is_favorite = request.is_favorite
        
    db.commit()
    db.refresh(db_image)
    return db_image

@app.delete("/images/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    """Delete an image record from the DB and file system"""
    db_image = db.query(models.ImageRecord).filter(models.ImageRecord.id == image_id).first()
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Delete from filesystem
    if os.path.exists(db_image.file_path):
        try:
            os.remove(db_image.file_path)
        except Exception as e:
            print(f"Error deleting file {db_image.file_path}: {e}")
            
    # Delete from database
    db.delete(db_image)
    db.commit()
    return {"status": "success", "message": "Image deleted"}
