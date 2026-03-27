import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_images(image_description, num_images):
    try:
        images = pipe(prompt=image_description, num_inference_steps=50, num_images_per_prompt=num_images).images
        return images
    except Exception as e:
        return str(e)

# Streamlit configuration
st.set_page_config(page_title="Stable Diffusion Image Generation Tool", page_icon=":camera:", layout="wide")

st.title("Stable Diffusion Image Generation Tool")
st.subheader("Powered by Hugging Face and Stable Diffusion")

# User inputs
img_description = st.text_input("Enter a description of your thoughts")
num_of_images = st.number_input("Select the number of images you want", min_value=1, max_value=10, value=1)

# Generate images on button click
if st.button("Generate Images now"):
    if img_description:
        with st.spinner("Generating images..."):
            try:
                # Generate images
                images = generate_images(img_description, num_of_images)
                
                if isinstance(images, str):
                    st.error(f"An error occurred: {images}")
                else:
                    # Display images
                    st.success("Images generated successfully!")
                    for i, image in enumerate(images):
                        st.image(image, caption=f"Image {i+1}", use_column_width=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a description to generate images.")
