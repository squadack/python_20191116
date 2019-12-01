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

print( formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) )
print( formatuj('ala ma $co', co='kota') )
print( formatuj('Nazywam $imie $nazwisko', imie='Piotr', nazwisko='GG') )

def test_wszystko():
    assert True







