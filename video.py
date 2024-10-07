# video_creation.py
import cv2
import os

def create_video(image_folder, video_name, fps=1):
    """Creates a video from a folder of images."""
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()  # Sort images by name to maintain order

    # Get the width and height from the first image
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
    print(f"Video created and saved as {video_name}")
