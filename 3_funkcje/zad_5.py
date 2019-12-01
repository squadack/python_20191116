"""
Zaimplementuj funkcję obliczającą silnie dla zadanej wartości.
Przykład użycia:
silnia(5)
120
"""

def silnia(n: int):
    if n < 0 or type(n) is not int:
        # return None # programista używający naszej funkcji będzie musiał dodatkowo sprawdzić czy nie dostał None
        raise ValueError('n musi byc intem i być większe od 0')

    wynik = 1

    for i in range(1, n + 1):
        wynik *= i

    return wynik

import pytest

def test_n_mniejsze_od_zera():
    with pytest.raises(ValueError):
        silnia(-10)

def test_n_zero():
    assert silnia(0) == 1

def test_n_wieksze_od_zero():
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 120
    assert silnia(6) == 720
    assert silnia(7) == 5040
    assert silnia(8) == 40320