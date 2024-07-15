import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    This function loads an image, prints its format,
    and its pixels content in RGB format.

    Args:
        path (str): the path of the image

    Returns:
        np.ndarray: numpy array of the image pixels
    """
    try:
        assert isinstance(path, str), "The path of image should be a string"
        # # Open Image using pillow library
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert('RGB')
        img = np.array(img)
        print(f"The shape of image is: {img.shape}")
        return img
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except FileNotFoundError:
        print("File not found")
    except Image.UnidentifiedImageError:
        print("You should give a path to a image file")
    except PermissionError:
        print(f"Error: Permission denied when trying to open file: {path}")
    except IOError:
        print(f"Error: Unable to open the image file at {path}.")
    except Exception as err:
        print(f"{Exception.__name__}: {err}")
    return np.array([])
