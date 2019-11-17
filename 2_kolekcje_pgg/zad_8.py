"""
Napisz program zliczający liczbę znaków w podanym przez
użytkownika napisie pomiędzy nawiasami <>. Nawiasy
mogę wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
4
"""

napis = input("Podaj napis: ")

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Zla liczba nawiasow! Ejże!')
    exit() # uruchomienie exit() powoduje natychmiastowe zatrzymanie programu

czy_zliczac = False
liczba_znakow = 0

for znak in napis:
    if znak == '<':
        czy_zliczac = True
    elif znak == '>':
        czy_zliczac = False
    elif czy_zliczac == True:
        liczba_znakow += 1

print(liczba_znakow)







