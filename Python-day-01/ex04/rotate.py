import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_crop(img: np.ndarray) -> np.ndarray:
    """
    This function crops an image from the center
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
        n_w, n_h, w, h = img.shape[1], img.shape[0], 400, 400
        s_x, s_y = (n_w - w) // 2, (n_h - h) // 2
        img = img[s_y: s_y + h, s_x: s_x + w]
        img = np.mean(img, axis=2, keepdims=True).astype(np.uint8)
        print(f"The shape of image is: {img.shape}")
        return img
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """
    This function rotate an image from the center

    Args:
        img (np.ndarray): 3D array of Gray Scale of the image

    Returns:
        np.ndarray: numpy array of the new image data
    """
    try:
        assert img is not None and isinstance(img, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert img.ndim == 3 and img.size, "Your image sould be a 3D list"
        img = Image.fromarray(img.squeeze(), 'L')
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img = np.array(img)
        return img
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def main():
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        img = ft_crop(img)
        print(img)
        img = ft_rotate(img)
        print(img)
        # # Display the image
        plt.imshow(img, cmap='gray')
        plt.axis('on')
        plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
