import numpy as np
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
        w, h = 400, 400
        s_x, s_y = (img.shape[1] - w) // 2, (img.shape[0] - h) // 2
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
        w, h = len(img[0]), len(img)
        rimg = np.array([[img[y][x][0] for y in range(h)] for x in range(w)])
        print(f"New shape after Transpose: {rimg.shape}")
        return rimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def main():
    try:
        path = "animal.jpeg"
        # Load the image
        img = ft_load(path)
        # Crop the image
        cimg = ft_crop(img)
        print(cimg)
        # Rotate the image
        rimg = ft_rotate(cimg)
        print(rimg)
        # Display Only the rotate image
        plt.imshow(rimg, cmap='gray')
        plt.axis('on')
        plt.show()
        # # # Display Both images
        # fig = plt.figure(figsize=(10, 20))
        # fig.add_subplot(2, 1, 1)
        # plt.imshow(img, cmap='gray')
        # plt.title("normal")
        # plt.axis('on')
        # fig.add_subplot(2, 1, 2)
        # plt.imshow(rimg, cmap='gray')
        # plt.title("Rotate")
        # plt.axis('on')
        # plt.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()
