from load_image import ft_load
from PIL import Image, ImageOps
import numpy as np

def ft_zoom(img_arr: np.ndarray, factor: int | float,
            start_px: tuple = (0, 0)) -> np.ndarray:

    """
    ft_zoom(path: str, zfactor: int | float, start_pixel: tuple) -> np.ndarray

    NOTE: start_pixel is an optional argument. Default value is (0, 0).

    Return a zoomed img arr based on the zfactor(zoom in factor)
    and start pixel (if specified).
    """

    try:
        if img_arr is None:
            raise AssertionError("img_arr is None")

        if not isinstance(img_arr, np.ndarray):
            raise AssertionError("expecting img_arr to be a numpy array")

        if not isinstance(factor, (int, float)):
            raise AssertionError("expecting factor to be an int")

        if not isinstance(start_px, tuple):
            raise AssertionError("expecting start_px to be a tuple")

        if not all([x >= 0 for x in start_px]):
            raise AssertionError("expecting start_px consists of " +
                                 "positive values only")

        if factor < 1:
            raise AssertionError("expecting factor to be greater than 0")

        # get the width and height of the img_arr, tuple unpacking operation
        (height, width, _) = img_arr.shape

        # calculate the new height and width based on the zoom factor
        new_dimension = min(height, width)
        new_height = int(new_dimension / factor)
        new_width = int(new_dimension / factor)

        left, upper = start_px
        right = left + new_width
        lower = upper + new_height

        if right > width or lower > height:
            raise AssertionError("zoomed region exceeds image dimension")

        # if i just do this -> [:, :, 0], i'm selecting all the values from
        # the first channel along the dimension. this will then become a
        # single list. if i do [:, :, 0:1], same but this will retain the
        # 3rd dimension
        zoomed_img_arr.show()
        zoomed_img_arr = img_arr[upper:lower, left:right, 0:1]
        print(f"New shape after slicing: {zoomed_img_arr.shape}" +
              f" or ({zoomed_img_arr.shape[0]}, {zoomed_img_arr.shape[1]})")
        return zoomed_img_arr
    except Exception as e:
        print(f"[ERROR]: {e}")


def main():
    try:
        path = 'animal.jpeg'
        # x, y = 400, 400
        old_img = ft_load(path)
        zoom = ft_zoom(old_img, 2, (0, 0))
        # img = Image.fromarray(old_img, 'RGB')
        # img = img.resize((img.size[0], img.size[1]))
        # left = abs(img.size[0] - x) // 2
        # top = abs(img.size[1] - y) // 2
        # right = left + x
        # bottom = top + y
        # img = img.crop((left, top, right, bottom))
        # img = img.resize((400, 400))
        # print(old_img)
        # nimg = np.array(img)
        # print(f"New shape after slicing: {nimg.shape} or {(nimg.shape[0], nimg.shape[1])}")
        # print(nimg)
        # img.show()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


if __name__ == "__main__":
    main()