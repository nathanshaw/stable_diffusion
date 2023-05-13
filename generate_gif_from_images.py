import os
import sys
from PIL import Image
import argparse

def create_gif(arg_dict):
    folder_path = arg_dict["path"]
    duration = arg_dict["delay"]
    fade = arg_dict["fade"]
    # Get all image files in the folder and sort them by filename
    images = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(folder_path, filename)
            images.append(Image.open(filepath).convert("RGBA"))

    # Create a new list of images with gradually increasing alpha values
    alpha_images = []
    alpha_step = 255 // len(images)
    for i, image in enumerate(images):
        alpha = alpha_step * i
        alpha_layer = Image.new("RGBA", image.size, (255, 255, 255, alpha))
        alpha_images.append(Image.alpha_composite(image.convert("RGBA"), alpha_layer))

    # Create the animated GIF
    gif_path = os.path.join(folder_path, "animation_dur_{}_fade_{}.gif".format(duration, str(fade)))
    alpha_images[0].save(gif_path, save_all=True, append_images=alpha_images[1:], duration=duration, loop=0)
    print("GIF saved to:", gif_path)

if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Create a fading GIF from a folder of images")
    parser.add_argument("--path", type=str, help="path to the folder containing images")
    parser.add_argument("--delay", type=float, default=0.2, help="delay between frames in the GIF")
    parser.add_argument("--fade", type=bool, default=True, help="If set to true, prorgram will alpha fade between each image in gif")
    # Parse command-line arguments
    args = vars(parser.parse_args())
    create_gif(args)
