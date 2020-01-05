import json

# json.load()
# json.loads()
# json.dump()
# json.dumps()

# obiekt = {"imie": "Jan", "cos": [None, 1, 2, 3]}
#
# napis = json.dumps(obiekt)
# print(napis)
# print(type(napis))
# print(repr(napis))
#
# # napis = "[1, 2, 3, false, true, null, {}]"
#
# wynik = json.loads(napis)
# print(type(wynik))
# print(wynik)
#
# with open("test.json") as plik:
#     obiekt = json.load(plik)
# print(obiekt)
# obiekt.append(123)
# with open("test.json", "w") as plik:
#     json.dump(obiekt, plik)

try:
    with open("pracownicy.json") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []
# mamy liste pracowników (z pliku, jeśli istniał)

op = input("Co chcesz zrobic? [d-dodaj, w-wypisz]: ")
if op == "d":
    pracownik = {}
    pracownik['imie'] = input("Podaj imię: ")
    pracownik['nazw'] = input("Podaj nazwisko: ")
    pracownik['rok'] = int(input("Podaj rok urodzenia: "))
    pracownik['pensja'] = int(input("Podaj pensję: "))
    pracownicy.append(pracownik)
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)
elif op == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"[{nr}] - {p['imie']} {p['nazw']}, rok urodzenia: {p['rok']}, pensja: {p['pensja']} PLN")
