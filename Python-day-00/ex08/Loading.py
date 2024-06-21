import os
import time
import sys


def ft_tqdm(lst: range) -> None:
    '''Decorate an iterable object, returning an iterator which acts \
exactly \nlike the original iterable, but prints a dynamically updating
progressbar every time a value is requested.'''

    c = '\u2588'
    mx = len(lst)
    lrg = os.get_terminal_size().columns - 25 - len(str(mx)) * 2
    spt, tt, it, step = "00:00", '?', '?it/s', 0
    # Turn off blinking cursor in command window
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    stl = time.time()
    for i in range(mx + 1):
        p = str(i * 100 // mx).rjust(3)
        ind = str(i).rjust(len(str(mx)))
        stop = time.time()
        st = int(stop - stl)
        spt = str(st // 60).zfill(2) + ':' + str(st % 60).zfill(2)
        if i == 1:
            tp = int(stop - stl) * mx
            tt = str(tp // 60).zfill(2) + ':' + str(tp % 60).zfill(2)
            step = round(float(stop - stl), 2)
            lrg -= 9
        if i >= 1:
            tp -= int(step)
            tt = str(tp // 60).zfill(2) + ':' + str(tp % 60).zfill(2)
            it = f'{ (i + 1) / (stop - stl):.2f}s/it'.rjust(9)
        lp = (c * (i * lrg // mx)).ljust(lrg)
        print(f'{p}%|{lp}| {ind}/{mx} [{spt}<{tt}, {it}]', end='\r')
        if i == mx:
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()
        yield i
