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

liczba_znakow = napis.index('>') - napis.index('<') - 1

print(liczba_znakow)







