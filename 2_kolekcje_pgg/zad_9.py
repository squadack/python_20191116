"""
Napisz program wyliczający kwotę należną za zakupiony towar na
podstawie podanej przez użytkownika wagi i nazwy produktu. Do
przechowywania informacji o cenie za kilogram danego produktu
użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.
"""

produkty = {
    'ziemniaki': 2.00,
    'pomidory': 8.50,
    'jablka': 2.99, # po ostatnim elemencie zwykle daje sie przecinek
}

print('Dostepne produkty w sklepie')
for produkt, cena_za_kg in produkty.items():
    print(f'{produkt} - {cena_za_kg:.2f} zł / kg')

co = input("Co chesz kupic z powyzszej listy? ")

if co not in produkty:
    print(f'Nie ma takiego produktu')
    # exit powoduje zatrzymanie programu
    # 0 - oznacza, że program zakończył się w porząku
    # każdy numer inny niż 0 oznacza, że coś poszło nie tak
    exit(1)

liczba_kg = float(input(f'Ile kilogramow produktu {co} chcesz kupic? '))

kwota = liczba_kg * produkty[ co ]
print(f'Za {liczba_kg} produktu {co} zaplacisz {kwota:.2f} zł')
