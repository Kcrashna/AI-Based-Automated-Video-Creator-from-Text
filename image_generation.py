# image_generation.py
from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path):
    """Generates an image based on the provided text prompt."""
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cpu")  
    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"Image generated and saved as {output_path}")
