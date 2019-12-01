"""
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
formatuj(
    'koszt $cena PLN',
    'kwota $cena brutto',
    cena=10,
)
'koszt 10 PLN\nkwota 10 brutto'
"""

def formatuj(*args, **kwargs):
    rezultat = []
    for napis in args:
        for nazwa_do_podmiany, wartosc in kwargs.items():
            napis = napis.replace(f'${nazwa_do_podmiany}', str(kwargs[nazwa_do_podmiany]))

        rezultat.append(napis)

    return '\n'.join(rezultat)

def test_wszystko():
    assert formatuj('Hello World!') == 'Hello World!'
    assert formatuj('Hello World!', imie='Piotr') == 'Hello World!'
    assert formatuj('Ala ma $co', co='kota') == 'Ala ma kota'
    assert formatuj('$kto najlepsze $co', kto='ALX', co='szkolenia') == 'ALX najlepsze szkolenia'
    assert formatuj('kwota $cena', 'wartość $cena', cena=10) == 'kwota 10\nwartość 10'
    assert formatuj(
        'Autor $imie $nazwisko',
        'Cześć $imie $nazwisko',
        imie='Piotr',
        nazwisko='GG') == 'Autor Piotr GG\nCześć Piotr GG'




