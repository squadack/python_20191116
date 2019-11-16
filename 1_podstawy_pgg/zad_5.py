"""
Napisz program obliczający koszt przejazdu z miasta A do B na
podstawie podanej przez użytkownika liczby kilometrów, ceny paliwa
oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.
Przykładowe komunikaty programu:
Miasto A: Warszawa
Miasto B: Gdańsk
Dystans Warszawa-Gdańsk: 420
Cena paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105 PLN
"""

# input ZAWSZE zwraca nam string (str)
miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
# dystans = input('Dystans ' + miasto_a + '-' + miasto_b + ': ')
dystans = int(input(f'Dystans {miasto_a}-{miasto_b}: '))
cena = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

koszt = dystans * spalanie / 100 * cena
# koszt = round(dystans * spalanie / 100 * cena, 2)

# format-specifier
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:_^10.2f} PLN')