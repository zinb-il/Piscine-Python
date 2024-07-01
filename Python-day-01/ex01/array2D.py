import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function slices a 2D List using numpy library
    and prints the old shape and the new shape

    Args:
        family (list): list to slice
        start (int): start value
        end (int): end value

    Returns:
        list: new list
    """
    try:
        assert isinstance(start, int), "The start should be an integer value"
        assert isinstance(end, int), "The end shoud be an integer value"
        assert isinstance(family, list), "Your first input should be a list"
        assert len(family), "Empty array to slice"
        assert all(isinstance(i, list) for i in family), "Your list \
elements should have the same type (list)"
        assert all(len(family[0]) == len(i) for i in family), "Your lists \
should have the same size"
        f = np.array(family)
        print(f"My shape is : {f.shape}")
        f = f[start: end]
        print(f"My new shape is : {f.shape}")
        return f.tolist()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as err:
        print(f"ExceptionError: {err}")
