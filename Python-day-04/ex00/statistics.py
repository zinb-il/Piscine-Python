from typing import Any, Iterable


def ft_len(lst: Iterable) -> int:
    """Calculate the length of an iterable.

    Args:
        lst (Iterable): The iterable object to measure.

    Returns:
        int: The length of the iterable.
    """
    count = 0
    for _ in lst:
        count += 1
    return count


def ft_sum(lst: list[float | int]) -> float:
    """Calculate the sum of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        float: The sum of all values in the list.
    """
    count = 0
    for i in lst:
        count += i
    return count


def ft_sort(lst: list[float | int]) -> list[float | int]:
    """Sort a list of numbers using bubble sort algorithm.

    Args:
        lst (list[float | int]): A list of numeric values to be sorted.

    Returns:
        list[float | int]: The sorted list in ascending order.
    """
    ch = False
    while not ch:
        for i in range(ft_len(lst) - 1):
            ch = True
            for j in range(i + 1, ft_len(lst)):
                if lst[i] > lst[j]:
                    ch = False
                    lst[i], lst[j] = lst[j], lst[i]
    return lst


def ft_count(lst: list[float | int], n: float | int) -> int:
    """Count the number of occurrences of a specific element in the list.

    Args:
        lst (list[float | int]): The list to search in.
        n (float | int): The value to count occurrences of.

    Returns:
        int: The number of times the specified element appears in the list.
    """
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count


def ft_mean(lst: list[float | int]) -> float:
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        float: The arithmetic mean of the list.
    """
    return ft_sum(lst) / ft_len(lst)


def ft_median(lst: list[float | int]) -> float:
    """Calculate the median of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        float: The median value of the list.
    """
    lis = ft_sort([i for i in lst])
    median = lis[ft_len(lis) // 2]
    if ft_len(lis) % 2 == 0:
        median = (median + lis[ft_len(lis) // 2 - 1]) // 2
    return median


def ft_quartile(lst: list[float | int]) -> list[int | float]:
    """Calculate the first (Q1) and third (Q3) quartiles of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        list[int | float]: A list containing [Q1, Q3].
    """
    lis = ft_sort([i for i in lst])
    eff = ft_sum([ft_count(lis, i) for i in set(lis)])
    q1 = eff / 4
    q1 = int(q1) if int(q1) == q1 else int(eff // 4 + 1)
    q3 = eff / 4 * 3
    q3 = int(q3) if int(q3) == q3 else int(eff // 4 * 3 + 1)
    return [float(lis[q1 - 1]), float(lis[q3 - 1])]


def ft_var(lst: list[float | int]) -> float:
    """Calculate the variance of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        float: The variance of the list.
    """
    lis = [i for i in lst]
    mean = ft_mean(lis)
    var = ft_sum([(i - mean) ** 2 for i in lis]) / ft_len(lis)
    return var


def ft_std(lst: list[float | int]) -> float:
    """Calculate the standard deviation of a list of numbers.

    Args:
        lst (list[float | int]): A list of numeric values.

    Returns:
        float: The standard deviation of the list.
    """
    return ft_var(lst) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate various statistical measures for a given set of numbers.

    This function can compute mean, median, quartiles, \
variance, and standard deviation.

    Args:
        *args: Variable length argument list of numeric values.
        **kwargs: Keyword arguments specifying which operations to perform.
            Valid keys are: "mean", "median", "quartile", "var", "std".
    """
    try:
        values = list(args)
        x = all(isinstance(i, float) for i in values)
        y = all(isinstance(i, int) for i in values)
        assert x or y, "All your values should be a folat or int"
        for op in kwargs.values():
            if not ft_len(values):
                print("ERROR")
                continue
            op = op.lower()
            if op == "mean":
                print(f"mean :{ft_mean(values)}")
            elif op == "median":
                print(f"median :{ft_median(values)}")
            elif op == "quartile":
                print(f"quartile :{ft_quartile(values)}")
            elif op == "var":
                print(f"var :{ft_var(values)}")
            elif op == "std":
                print(f"std :{ft_std(values)}")
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"ExceptionError: {err}")
