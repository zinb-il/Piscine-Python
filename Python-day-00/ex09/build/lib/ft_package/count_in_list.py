from typing import Iterable, TypeVar

T = TypeVar('T')

def count_in_list(__it: Iterable[T],__targ:T)->int:
    """
    Compte les occurrences de l'élément cible dans la table itérative.
    
    Paramètres :
    iterable (Iterable[T]) : Le tableau itératif des éléments à rechercher.
    target (T) : L'élément cible à compter dans l'itérable.

    Retourne :
    int : Le nombre d'occurrences de l'élément cible dans l'itérable.
    """
    return __it.count(__targ)