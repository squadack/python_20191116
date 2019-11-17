"""
Napisz program zliczający liczbę wystąpień samogłosek (a, e, i,
o, u, y) w podanym przez użytkownika napisie.
"""

napis = input("Podaj napis: ")

samogloski = ['a', 'e', 'i', 'o', 'u'] # lista
samogloski = ('a', 'e', 'i', 'o', 'u') # tupla
samogloski = 'aeiou'
ile_samoglosek = 0

for samogloska in samogloski:
    # ile_samoglosek += napis.lower().count(samogloska) # method chaining
    napis_malymi_literami = napis.lower()
    liczba = napis_malymi_literami.count(samogloska)
    ile_samoglosek = ile_samoglosek + liczba

print(f'W napisie "{napis}" jest {ile_samoglosek} samogłosek')
