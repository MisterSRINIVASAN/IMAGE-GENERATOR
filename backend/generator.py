import torch
from diffusers import StableDiffusionPipeline
import os
import uuid
from PIL import Image

# Automatically use CUDA (GPU) if available, otherwise fall back to CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cpu":
    print("WARNING: CUDA not available. Falling back to CPU. Image generation will be very slow.")

print(f"Loading model to {device}...")
try:
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    pipe = pipe.to(device)
    # Enable memory saving features if needed
    # pipe.enable_attention_slicing()
except Exception as e:
    print(f"Error loading model: {e}")
    pipe = None

IMAGES_DIR = "generated_images"

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

def generate_image(prompt: str) -> str:
    """
    Generate an image from a prompt, save it to disk, and return the path.
    """
    if pipe is None:
        raise RuntimeError("Stable Diffusion model failed to load.")
    
    # We will only generate 1 image per call for simplicity in saving
    result = pipe(prompt=prompt, num_inference_steps=50, num_images_per_prompt=1)
    image = result.images[0]
    
    # Create a unique filename
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(IMAGES_DIR, filename)
    
    image.save(filepath)
    return filepath
