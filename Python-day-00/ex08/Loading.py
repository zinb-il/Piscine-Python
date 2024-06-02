import os
import time
from time import sleep


def ft_tqdm(lst: range) -> None:
    '''Decorate an iterable object, returning an iterator which acts \
exactly \nlike the original iterable, but prints a dynamically updating
progressbar every time a value is requested.'''


    c = '-'
    mx = len(lst)
    l = os.get_terminal_size().columns - 24 - len(str(mx)) * 2
    for i in range(mx + 1):
        start = time.time()
        sleep(0.005)
        p = str(i * 100 // mx).rjust(3)
        # ps = " " * (3 - len(p))
        lp = i * l // mx
        ls = " " * (l - lp)
        ind = " " * (len(str(mx)) - len(str(i)))
        stop = time.time()
        print(f'{p}%|{c * lp}{ls}| {ind}{i}/{mx} {stop - start:.2f}', end='\r')
        yield i
