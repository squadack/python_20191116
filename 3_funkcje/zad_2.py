"""
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}
wiecej_niz('', 3) -> {} # dostaje pusty zbior
"""


def wiecej_niz(napis, ile_znakow):
    wystapienia = dict()
    for litera in napis: # zliczam sobie wystapienia poszczegolnych liter w napisie
        if litera in wystapienia:
            wystapienia[litera] += 1
        else:
            wystapienia[litera] = 1

    # sprawdzam, ktore ze zliczonych liter spelniaja warunek i tylko te oddam z funkcji
    wynik = set()
    for litera, liczba_wystapien in wystapienia.items():
        if liczba_wystapien > ile_znakow:
            wynik.add(litera)

    return wynik


def test_dla_pustego_napisu():
    assert wiecej_niz('', 3) == set()

def test_dla_niepustego_napisu():
    assert wiecej_niz('aaaabbbccd', 2) == {'a', 'b'}

