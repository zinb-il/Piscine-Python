import os
import time
import sys


def ft_hide_cursor():
    '''Disable blinking cursor in control window'''
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def ft_show_cursor():
    '''Disable blinking cursor in control window'''
    sys.stdout.write("\033[?25h")
    sys.stdout.write("\n")
    sys.stdout.flush()


def ft_tqdm(lst: range) -> None:
    '''Decorate an iterable object, returning an iterator which acts \
exactly \nlike the original iterable, but prints a dynamically updating
progressbar every time a value is requested.'''
    # Le symbole à afficher dans la barre de recherche
    c = '\u2588'
    mx = len(lst)
    spt, tt, it, rmnt, cr = "00:00", '?', '?it/s', 0, ''
    # Désactiver le curseur clignotant dans la fenêtre de commande
    ft_hide_cursor()
    stl = time.time()
    for i in range(mx + 1):
        lrg = os.get_terminal_size().columns - 25 - len(str(mx))
        p = str(i * 100 // mx).rjust(3)
        ind = str(i)
        stop = time.time()
        st = int(stop - stl)
        spt = str(st // 60).zfill(2) + ':' + str(st % 60).zfill(2)
        if i >= 1:
            rmnt = i / st if st else 0
            cr = 'it/s' if rmnt > 1 else 's/it'
            it = f'{rmnt:.2f}{cr}'.rjust(9)
            rmnt = int((mx - i) / rmnt) if rmnt else 0
            tt = str(rmnt // 60).zfill(2) + ':' + str(rmnt % 60).zfill(2)
            lrg -= len(it) - 6 + len(tt)
        lrg -= len(ind)
        lp = (c * (i * lrg // mx)).ljust(lrg)
        print(f'{p}%|{lp}| {ind}/{mx} [{spt}<{tt}, {it}]', end='\r')
        if i == mx:
            # Activer le curseur  dans la fenêtre de commande
            ft_show_cursor()
        yield i
