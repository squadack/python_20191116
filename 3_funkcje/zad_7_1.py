"""
Zaimplementuj funkcję przycinającą listę na podstawie podanego
warunku początkowego oraz końcowego:
Przykład użycia:
przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x > 3,
    stop=lambda x: x == 6,
)
[4, 5, 6]
"""

def przytnij(data, start, stop):
    rezultat = []

    for wartosc in data:
        if rezultat or start(wartosc):
            rezultat.append(wartosc)
            if stop(wartosc):
                break

    return rezultat

def test_zaden():
    assert przytnij(
                data=[1, 2, 3, 4, 5, 6, 7],
                start=lambda x: False,
                stop=lambda x: x == 6,
                ) == []

def test_ostatni():
    assert przytnij(
                data=[1, 2, 3, 4, 5, 6, 7],
                start=lambda x: x == 7,
                stop=lambda x: x == 6,
                ) == [7]

def test_wieksze_od_3_skoncz_na_6():
    assert przytnij(
                data=[1, 2, 3, 4, 4, 5, 6, 7],
                start=lambda x: x > 3,
                stop=lambda x: x == 6,
                ) == [4, 4, 5, 6]

def test_wieksze_zacznij_od_2_skoncz_na_mniejszej_niz_7():
    assert przytnij(
                data=[3, 2, 3, 6, 3, 4, 7],
                start=lambda x: x == 2,
                stop=lambda x: x < 7,
                ) == [2]

def test_wieksze_zacznij_od_mniejszej_niz_7_skoncz_na_2():
    assert przytnij(
                data=[9, 1, 6, 189, 4, 7, 2, 4],
                start=lambda x: x < 7,
                stop=lambda x: x == 2,
                ) == [1, 6, 189, 4, 7, 2]
