"""
Napisz program obliczający średnią wartość temperatury w danym
tygodniu na podstawie temperatur wprowadzonych przez
użytkownika.
"""

suma_temperatur = 0
numer_dnia = 1

while numer_dnia <= 7:
    suma_temperatur += int(input(f"Podaj temperaturę z dnia {numer_dnia}"))
    numer_dnia += 1

srednia_temperatur = suma_temperatur / 7

print(f"Srednia temperatura w tym tygodniu to {srednia_temperatur}")

