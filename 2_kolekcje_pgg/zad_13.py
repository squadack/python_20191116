"""
W sesji interaktywnego środowiska stwórz następujące struktury
danych korzystając ze skróconej wersji zapisu:
- listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
- zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
- słownik mapujący napisy na ich długość powstały ze zbioru napisów
"""
# listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
# a = [ x for x in range(0.0, 1.0, 0.1) ] # TypeError: 'float' object cannot be interpreted as an integer
a = [ x/10 for x in range(0, 11) ]
print(a)

# zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian
# - w przedziale od -10 do 10
b = { (x, x**2, x**3) for x in range(-10, 11) }
print(b)

# słownik mapujący napisy na ich długość powstały ze zbioru napisów
c = {'ala', 'krysia', 'Hello world!', 'Ala ma kota', 'Kot ma kompilator'}
dlugosci = { napis: len(napis) for napis in c }
print(dlugosci)