import os
import sys
from PIL import Image

def create_gif(folder_path, duration):
    images = []
    # Get all files in the folder and sort them by file name
    files = sorted(os.listdir(folder_path))
    for file in files:
        if file != ".DS_Store":
            # Load each image and append it to the list
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                image = Image.open(file_path)
                images.append(image)

    # Create the animated GIF
    gif_path = os.path.join(folder_path, "animation.gif")
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration*1000, loop=0)

if __name__ == "__main__":
    # Get command line arguments
    folder_path = sys.argv[1]
    duration = float(sys.argv[2])
    # Create the animated GIF
    create_gif(folder_path, duration)