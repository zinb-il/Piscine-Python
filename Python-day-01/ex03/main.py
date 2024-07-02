import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

def load_image(path):
    try:
        image = Image.open(path)
        return np.array(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

def print_image_info(image):
    try:
        print(f"The shape of the image is: {image.shape}")
        print("The pixel content of the image:")
        print(image)
    except Exception as e:
        print(f"Error printing image info: {e}")
        sys.exit(1)

def zoom_image(image, zoom_factor=0.5):
    try:
        h, w = image.shape[:2]
        new_h, new_w = int(h * zoom_factor), int(w * zoom_factor)
        start_x, start_y = (w - new_w) // 2, (h - new_h) // 2
        zoomed_image = image[start_y:start_y + new_h, start_x:start_x + new_w]
        return zoomed_image
    except Exception as e:
        print(f"Error zooming image: {e}")
        sys.exit(1)

def display_image(image, title="Image"):
    try:
        plt.imshow(image)
        plt.title(title)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")
        sys.exit(1)

def main():
    image_path = "animal.jpeg"
    image = load_image(image_path)
    print_image_info(image)

    zoomed_image = zoom_image(image)
    print(f"New shape after slicing: {zoomed_image.shape}")
    print("The pixel content of the zoomed image:")
    print(zoomed_image)

    display_image(zoomed_image, title="Zoomed Image")

if __name__ == "__main__":
    main()