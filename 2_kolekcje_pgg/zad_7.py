"""
Napisz program zliczający liczbę wystąpień samogłosek (a, e, i,
o, u, y) w podanym przez użytkownika napisie.
"""

napis = input("Podaj napis: ")

samogloski = ['a', 'e', 'i', 'o', 'u'] # lista
samogloski = ('a', 'e', 'i', 'o', 'u') # tupla
samogloski = 'aeiou'
ile_samoglosek = 0

for znak in napis.lower():
    if znak in samogloski:
        ile_samoglosek += 1

print(f'W napisie "{napis}" jest {ile_samoglosek} samogłosek')
