"""
Napisz program obliczający średnią wartość z podanych przez
użytkownika liczba. Do przechowywania liczb użyj listy. Pozwól na
wprowadzenie maksymalnie 10 liczb. Skorzystaj z funkcji
wbudowanej sum().
"""

liczby = [] # tworzy pustą listę
liczby = list() # tworzy pustą listę

while len(liczby) < 10:
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)

print(liczby)
srednia = sum(liczby) / len(liczby)
print(f'Średnia z wprowadzonych liczb to {srednia}')

