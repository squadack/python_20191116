"""
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}
wiecej_niz('', 3) -> {} # dostaje pusty zbior
"""


def wiecej_niz(napis, ile_znakow):
    wynik = set()
    for znak in napis:
        if napis.count(znak) > ile_znakow:
            wynik.add(znak)

    return wynik


def test_dla_pustego_napisu():
    assert wiecej_niz('', 3) == set()

def test_dla_niepustego_napisu():
    assert wiecej_niz('aaaabbbccd', 2) == {'a', 'b'}

