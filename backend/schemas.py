from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ImageBase(BaseModel):
    prompt: str

class ImageCreate(ImageBase):
    num_images: int = 1

class ImageUpdate(BaseModel):
    is_favorite: Optional[bool] = None

class ImageResponse(ImageBase):
    id: int
    file_path: str
    is_favorite: bool
    created_at: datetime

    class Config:
        from_attributes = True
