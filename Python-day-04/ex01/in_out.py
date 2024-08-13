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
    """Create a closure that applies a function repeatedly to an initial value.

    Args:
        x (int | float): The initial value to start the sequence.
        function (Callable[int | float]): A function to apply repeatedly.

    Returns:
        Callable[float]: function that when called, applies the given function
        to the current value and returns the result.
    """
    count = 0

    def inner() -> float:
        """Apply the function to the current count and return the result.

        This inner function maintains state between calls, applying the
        outer function's `function` argument to `count` on each invocation.

        Returns:
            float: The result of applying the function to the current count.
        """
        nonlocal count
        if not count:
            count = x
        count = function(count)
        return count
    return inner
