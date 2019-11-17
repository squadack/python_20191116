"""
Napisz program obliczający średnią wartość temperatury w danym
tygodniu na podstawie temperatur wprowadzonych przez
użytkownika.
"""

suma_temperatur = 0
numer_dnia = 1
LICZBA_DNI_TYGODNIA = 7

while numer_dnia <= LICZBA_DNI_TYGODNIA:
    suma_temperatur += int(input(f"Podaj temperaturę z dnia {numer_dnia}: "))
    numer_dnia += 1

srednia_temperatur = suma_temperatur / LICZBA_DNI_TYGODNIA

print(f"Srednia temperatura w tym tygodniu to {srednia_temperatur}")

