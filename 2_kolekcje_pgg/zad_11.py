"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
iloczynu.
"""
# liczby_parzyste = {} # UWAGA! To stworzy nowy słownik a nie zbiór!

# liczby_parzyste = set()
# for x in range(0, 101, 2):
#     liczby_parzyste.add(x)

liczby_parzyste = set(range(0, 101, 2))


liczby = set()
while True:
    liczba = input('Podaj liczbę: ')
    if liczba == 'koniec':
        break
    else:
        liczby.add(int(liczba))

print(f'Unikalnych liczb wprowadziles: {len(liczby)}')
print(f'Wprowadzone liczby parzyste od 0 do 100: {liczby & liczby_parzyste}')
print(f'Liczba wprowadzonych liczb parzystych od 0 do 100: {len(liczby & liczby_parzyste)}')
