from typing import Any, Iterable


def ft_len(lst: Iterable) -> int:
    """this function claculate the length of a iterable

    Args:
        Iterable: iterable object

    Returns:
        int: the length of the list
    """
    count = 0
    for i in lst:
        count += 1
    return count


def ft_sum(lst: list[float | int]) -> float:
    """this function claculate the sum of a list of number

    Args:
        lst (list[float  |  int]): values

    Returns:
        float: the sum of the list
    """
    count = 0
    for i in lst:
        count += i
    return count


def ft_sort(lst: list[float | int]) -> list[float | int]:
    """this function sort a list using buble sort

    Args:
        lst (list[float  |  int]): values

    Returns:
        list[float | int]: the sorted list
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
    """this function  returns the number of times the specified element \
appears in the list

    Args:
        lst (list[float  |  int]): list to search in
        n (float  |  int): number to serach number of times

    Returns:
        int: the number of occourence
    """
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count


def ft_mean(lst: list[float | int]) -> float:
    """this function calculate the mean of a list of number

    Args:
        lst (list[float  |  int]): values
    Returns:
        float: the mean
    """
    return ft_sum(lst) / ft_len(lst)


def ft_median(lst: list[float | int]) -> float:
    """this function calculate the mean of a list of number

    Args:
        lst (list[float  |  int]): values
    Returns:
        float: the median
    """
    lis = ft_sort([i for i in lst])
    median = lis[ft_len(lis) // 2]
    if ft_len(lis) % 2 == 0:
        median = (median + lis[ft_len(lis) // 2 - 1]) // 2
    return median


def ft_quartile(lst: list[float | int]) -> list[int | float]:
    """this function calculate the Quartile (25% and 75%) of a list of number

    Args:
        lst (list[float  |  int]): values
    Returns:
        list[int | float] : value of q1 and q3
    """
    lis = ft_sort([i for i in lst])
    eff = ft_sum([ft_count(lis, i) for i in set(lis)])
    q1 = eff / 4
    q1 = int(q1) if int(eff / 4) == q1 else int(eff // 4 + 1)
    q3 = eff / 4 * 3
    q3 = int(q3) if int(eff / 4 * 3) == q3 else int(eff // 4 * 3 + 1)
    return [float(lis[q1 - 1]), float(lis[q3 - 1])]


def ft_var(lst: list[float | int]) -> float:
    """this function calculate the varition of a list of number

    Args:
        lst (list[float  |  int]): values
    Returns:
        float: variation
    """
    lis = [i for i in lst]
    mean = ft_mean(lis)
    var = ft_sum([(i - mean) ** 2 for i in lis]) / ft_len(lis)
    return var


def ft_std(lst: list[float | int]) -> float:
    """this function calculate the Standard Deviation of a list of number

    Args:
        lst (list[float  |  int]): values
    Returns:
        float: standard deviation
    """
    return ft_var(lst) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """This function calculates  Mean, Median,Quartile (25% and 75%), \
Standard Deviation and Variance

        Args:
            *args(tuple(int)): values
            **kwargs(dictinnary{str}): operation to calculate
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
