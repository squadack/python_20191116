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


import pytest

def test_n_mniejsze_od_zera():
    with pytest.raises(ValueError):
        silnia(-10)

def test_n_zero():
    pass

def test_n_wieksze_od_zero():
    pass