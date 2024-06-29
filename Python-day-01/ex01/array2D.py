import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        f = np.array(family)
        assert isinstance(start, int), "The start shoud be an integer value"
        assert isinstance(start, int), "The end shoud be an integer value"
        print("")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as err:
        print(f"ExceptionError: {err}")
