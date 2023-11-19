from typing import Callable, Iterable


def ft_filter(__func: Callable | None, __it: Iterable) -> filter:
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if __func is None:
        __func = bool
    return (i for i in __it if __func(i))
