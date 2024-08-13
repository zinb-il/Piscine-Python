from typing import Any


def callLimit(limit: int):
    """Create a decorator that limits the number \
of times a function can be called.

    Args:
        limit (int): The maximum number of times \
the decorated function can be called.
    """
    count = 0

    def callLimiter(function):
        """Decorate a function to limit its number of calls.

        Args:
            function (): The function to be decorated.
        """
        def limit_function(*args: Any, **kwds: Any):
            """Execute the original function if the call \
limit hasn't been reached.

            Args:
                *args: Variable length argument list.
                **kwds: Arbitrary keyword arguments.
            """
            try:
                nonlocal count
                if count >= limit:
                    raise Exception(f"{function} call too many times")
                count += 1
                return function(*args, **kwds)
            except Exception as err:
                print(f"Error: {err}")
            return None
        return limit_function
    return callLimiter
