import numpy as np


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """This function returns the BMI (Body Mass Index) of a list \
of weights and heights

    Args:
        h (list[int  |  float]): Heights value
        w (list[int  |  float]): Weights value

    Returns:
        list[int | float]: list of BMI
    """
    try:
        h, w = np.array(h), np.array(w)
        assert h.dtype.kind in 'fi' and w.dtype.kind in 'fi', "Height and \
weight must be integers or floats."
        assert h.shape == w.shape, "Height and weight list \
must be of the same shape and size"
        assert h.size and w.size, "Height and weight lists must not be empty."
        assert np.all(h > 0), "All height values must be positive"
        assert np.all(w > 0), "All weight values must be positive"
        return (w / h**2).tolist()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function returns bool values for a list that is bigger than the limit

    Args:
        bmi (list[int | float]): list of given BMI
        limit (int): limit to compare

    Returns:
        list[bool]: bool values
    """
    try:
        bmi = np.array(bmi)
        assert bmi.size, "Your list is empty"
        assert isinstance(limit, int), "The limit shoud be an integer value"
        assert bmi.dtype.kind in 'fi', "Your list values must be \
integers or floats."
        return (bmi > limit).tolist()
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")
