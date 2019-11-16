"""
Napisz program wyliczający kwotę należną za zakupiony towar na
podstawie ceny za kilogram oraz liczby zakupionych kilogramów. Do
przechowywania informacji o cenie oraz liczbie kilogramów użyj
zmiennych. Wypisz wszystkie informacje na konsolę.
Przykładowy komunikat programu:
Cena za kg: 10.0
Waga: 2.5
Należność: 25.0
"""

cena = 10.0
waga = 2.5
naleznosc = cena * waga

print('Cena za kg:', cena, 'zł')
print('Cena za kg: ' + str(cena) + ' zł')
print('Waga:', waga)
print('Należność:', naleznosc)

# f-string - wykorzystuje sie do budowania napisow, ktore zawieraja zmienne
print(f'Cena za kg: {cena} zł')
print(f'Waga: {waga} kg')
print(f'Należność: {naleznosc} zł')
