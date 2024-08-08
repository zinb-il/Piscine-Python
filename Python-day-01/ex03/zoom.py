import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_zoom(img: np.ndarray) -> np.ndarray:
    """
    This function zooms and crops an image from the center
    and converts it from RGB to Grayscale mode.

    Args:
        img (np.ndarray): 3D array of RGB colors of the image

    Returns:
        np.ndarray: numpy array of the new image data
    """
    try:
        assert img is not None and isinstance(img, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert img.ndim == 3 and img.size, "Your image sould be a 3D list"
        z_f, w, h = 1.2, 400, 400
        n_w, n_h = int(img.shape[1] * z_f), int(img.shape[0] * z_f)
        s_x, s_y = (n_w - w) // 2,  h // 2
        img1 = Image.fromarray(img, 'RGB')
        img1 = img1.resize((n_h, n_w))
        img1 = np.array(img1)
        img1 = img1[s_y: s_y + h, s_x: s_x + w]
        img1 = np.mean(img1, axis=2, keepdims=True).astype(np.uint8)
        n_w, n_h = img1.shape[:2]
        print(f"New shape after slicing: {img1.shape} or {(n_h, n_w)}")
        return img1
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def main():
    try:
        path = 'animal.jpeg'
        # #Load the image
        img = ft_load(path)
        print(img)
        # #Zoom, crop and convert to grayscale image
        z_img = ft_zoom(img)
        print(z_img)
        ###############################################
        # #Display the image using PIl library
        # img = Image.fromarray(z_img.squeeze(), 'L')
        # img.show()
        ###############################################
        # # Display the image
        plt.imshow(z_img, cmap='gray')
        plt.axis('on')
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
