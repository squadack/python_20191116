"""
Napisz program zliczający liczbę wystąpień każdego znaku w
podanym przez użytkownika napisie.
ala ma kota
'a' - 4
'l' - 1
'm' - 1
'k' - 1
'o' - 1
't' - 1
' ' - 2
"""

napis = input("Podaj napis do zliczenia liczby znaków: ")
wystapienia = {}

# for znak in napis:
#     if znak not in wystapienia:
#         wystapienia[znak] = 1
#     else:
#         wystapienia[znak] += 1

for znak in napis:
    if znak not in wystapienia:
        wystapienia[znak] = 0

    wystapienia[znak] += 1

print()

# sorted(wystapienia.items()) - sortuje listę tupli po pierwszej elemencie tupli
# czyli po kluczu z naszego słownika, bo ten jest umieszczony jako pierwszy element w tupli
for litera, liczba_wystapien in sorted(wystapienia.items()):
    print(f'{litera} = {liczba_wystapien}')