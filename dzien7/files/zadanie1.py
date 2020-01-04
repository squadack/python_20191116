# napis = f.read()
# print(f.readlines())
# for x in f:
#     print(x)

# f = open("plik.txt")
# print(f.read())
# f.close()
while True:
    nazwa = input("Podaj nazwe pliku: ")
    try:
        with open(nazwa, encoding="utf-8") as plik:
            print(plik)
            for nr, linia in enumerate(plik, 1):
                print(f"{nr:5}: {linia}", end="")
        break
    except FileNotFoundError:
        print("Nie ma takiego pliku!")
