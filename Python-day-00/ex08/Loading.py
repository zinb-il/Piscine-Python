import os
from time import sleep


def ft_tqdm(lst: range) -> None:
    '''Decorate an iterable object, returning an iterator which acts \
exactly \nlike the original iterable, but prints a dynamically updating
progressbar every time a value is requested.'''


    c = '\u2588'
    mx = len(lst)
    l = os.get_terminal_size().columns - 8 - len(str(mx)) * 2
    for i in range(mx + 1):
        p = str(i * 100 // mx)
        ps = " " * (3 - len(p))
        lp = i * l // mx
        ls = " " * (l - lp)
        ind = " " * (len(str(mx)) - len(str(i)))
        print(f'{ps}{p}%|{c * lp}{ls}| {ind}{i}/{mx}', end='\r')
        if i == mx: print()
        yield i
