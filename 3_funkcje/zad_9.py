"""
Zaimplementuj dekorator wypisujący wywołanie danej funkcji
(nazwa i argumenty) oraz czas jej wykonania.
Przykład użycia:
@log
def foo(arg):
return f'To jest {arg}'
"""

import time

def log(funkcja_do_udekorowania):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        stop = time.time()
        czas_dzialania = stop - start
        print(f'Czas dzialania funkcji {funkcja_do_udekorowania.__name__} to {czas_dzialania} sekund')
        return wynik

    return wrapper

@log
def silnia(n: int):
    if n < 0 or type(n) is not int:
        raise ValueError('n musi byc intem i być większe od 0')

    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

print( silnia(50000) )