# main.py
import os
from text_processing import extract_keywords
from image_generation import generate_image
from video import create_video
from audio import create_audio

def main(text_input):
    # Extract keywords or summarize text
    summary = extract_keywords(text_input)
    print(f"Extracted Summary: {summary}")

    # Create a directory to store generated images
    image_folder = "generated_images"
    os.makedirs(image_folder, exist_ok=True)

    # Generate image based on the summary
    image_filename = os.path.join(image_folder, "image_1.png")  # You can generate multiple images in a loop
    generate_image(summary, image_filename)

    # Create a video from the generated images
    create_video(image_folder, "output_video.mp4", fps=1)

    # Generate audio from the summary
    create_audio(summary, "output_audio.mp3")

if __name__ == "__main__":
    user_input = input("Enter your text: ")
    main(user_input)
