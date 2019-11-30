"""
Napisz funkcję sprawdzającą, czy dane liczba jest liczbą pierwszą.
Przykład użycia:
czy_jest_pierwsza(10)
False
czy_jest_pierwsza(17)
True
"""

def czy_jest_pierwsza(liczba: int) -> bool:
    """
    Funkcja sprawdza czy liczba jest pierwsza, tzn. że liczba jest tylko podzielna przez 1
    i samą siebie. Dodatkowo musi być większa od 1.
    :param liczba:
    :return:
    """
    if liczba <= 1 or type(liczba) is not int:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True # uwaga na poziom wciecia!!!


print(czy_jest_pierwsza(3.14))
print(czy_jest_pierwsza(10))
print(czy_jest_pierwsza(11))
print(czy_jest_pierwsza(9))

# wazne, żeby nasza funkcja do testowania zaczynała się od test_
def test_czy_liczba_jest_pierwsza():
    liczba = 5
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == True

def test_liczb_pierwszych():
    assert czy_jest_pierwsza(5) == True
    assert czy_jest_pierwsza(13) is True
    assert czy_jest_pierwsza(11)


def test_liczb_nie_pierwszych():
    assert czy_jest_pierwsza(-1) == False
    assert czy_jest_pierwsza(1) == False
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(9) == False




