def square(x: int | float) -> int | float:
    """this function calculate the square of a number

    Args:
        x (int | float): the to calucule its square

    Returns:
        int | float: the square of the number
    """
    try:
        assert isinstance(x, int) or isinstance(x, float), "The \
number should int or float"
        return x ** 2
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def pow(x: int | float) -> int | float:
    """this function calculate the exponentiation of number by himself

    Args:
        x (int | float): the to calucule its exponentiation

    Returns:
        int | float: the exponentiation
    """
    try:
        assert isinstance(x, int) or isinstance(x, float), "The \
number should int or float"
        return x ** x
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        return function(x)
    return inner
