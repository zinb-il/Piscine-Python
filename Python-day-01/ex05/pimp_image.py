import numpy as np


def ft_invert(array) -> np.ndarray:
    """This function inverts an RGB image.

    Args:
        array (np.ndarray): RGB array of the image.

    Returns:
        np.ndarray: RGB array of the inverted image.
    """
    try:
        assert array is not None and isinstance(array, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert array.ndim == 3 and array.size, "Your image sould be a 3D list"
        invimg = array.copy()
        invimg = 255 - invimg
        print(f"The shape of image is: {invimg.shape}")
        print(invimg)
        return invimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def ft_red(array) -> np.ndarray:
    """This function converts an RGB image to red.

    Args:
        array (np.ndarray): RGB array of the image.

    Returns:
        np.ndarray: RGB array of the red image.
    """
    try:
        assert array is not None and isinstance(array, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert array.ndim == 3 and array.size, "Your image sould be a 3D list"
        rimg = array.copy()
        rimg[:, :, 1] = 0
        rimg[:, :, 2] = 0
        print(f"The shape of image is: {rimg.shape}")
        print(rimg)
        return rimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def ft_green(array) -> np.ndarray:
    """This function converts an RGB image to green.

    Args:
        array (np.ndarray): RGB array of the image.

    Returns:
        np.ndarray: RGB array of the green image.
    """
    try:
        assert array is not None and isinstance(array, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert array.ndim == 3 and array.size, "Your image sould be a 3D list"
        gimg = array.copy()
        gimg[:, :, 0] = 0
        gimg[:, :, 2] = 0
        print(f"The shape of image is: {gimg.shape}")
        print(gimg)
        return gimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def ft_blue(array) -> np.ndarray:
    """This function converts an RGB image to blue.

    Args:
        array (np.ndarray): RGB array of the image.

    Returns:
        np.ndarray: RGB array of the blue image.
    """
    try:
        assert array is not None and isinstance(array, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert array.ndim == 3 and array.size, "Your image sould be a 3D list"
        bimg = array.copy()
        bimg[:, :, 0] = 0
        bimg[:, :, 1] = 0
        print(f"The shape of image is: {bimg.shape}")
        print(bimg)
        return bimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def ft_grey(array) -> np.ndarray:
    """This function converts an RGB image to grey.

    Args:
        array (np.ndarray): RGB array of the image.

    Returns:
        np.ndarray: RGB array of the grey image.
    """
    try:
        assert array is not None and isinstance(array, np.ndarray), "Your \
image sould be a 3D list of rgb colors"
        assert array.ndim == 3 and array.size, "Your image sould be a 3D list"
        gimg = array.copy()
        arr = (gimg[:, :, 0] / 3 + gimg[:, :, 1] / 3 + gimg[:, :, 2] / 3)
        arr = arr.astype(np.uint8)
        gimg = arr[:, :, np.newaxis]
        print(f"The shape of image is: {gimg.shape}")
        print(gimg)
        return gimg
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")
