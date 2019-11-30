# KOLEKCJE / Struktury danych

# ==== TUPLA ====

a = (1, 2, 3)
b = (1, 3.14, 'ala', True)
c = ( (1, 2), ('a', 'b', 'c') )

print(a)
print(b)
print(c)

d = (100) # UWAGA! Python potraktował to jako int a nie tuplę
print(d)
print(type(d))

# tupla jednoelementowa
e = (100,)
print(e)
print(type(e))

# pusta tupla
f = ()
print(f)
print(type(f))

g = tuple()
print(g)
print(type(g))

# wycinanie, wyciąganie wartości z tupli
# indeksy/klucze w tupli zaczynają się od 0
# x[start:stop-1:krok]
x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

print( x[0] ) # a
print( x[5] ) # f
print( x[1:3] ) # lewostronnie domkniety a prawostronnie otwarty, od 1 do 2 włącznie
print( x[2:6] ) # c, d, e, f
print( x[-1] )
print( x[-4:-1] )
print( x[1:] )
print( x[:4] )
print( x[:-2] )
print( x[::2] )
print( x[::-1] )
print( x[::-2] )

# przydatne metody
print( len(x) )
print( 'b' in x )
print( 'z' in x )

f = (1, 2, 3, 4, 5)
print(min(f))
print(max(f))
print(sum(f))

a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)

# d = a * b
d = a * 3
print(d)

a = ('a', 'b', 'd')
# a[2] = 'c' # tupli nie możemy zmieniać po utworzeniu
print(a)

# ==== LISTY ====
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# operator [] działa dokładnie tak samo
print(a)
print(a[0]) # 10
print(a[-1]) # 100

a[0] = -1
print(a)

a.append(110) # dokłada 110 na koniec listy
print(a)

a.insert(1, 12) # wklada na index 1 wartosc 12 i przesuwa cala reszte o jeden
print(a)

a[0:2] = [1, 2]
print(a)

a[0:2] = [1, 2, 3, 4]
print(a)

# a.append([120, 130, 140])
a.extend([120, 130, 140])
print(a)

del(a[0])
print(a)

del(a[0:2])
print(a)

del(a[-2:])
print(a)

del(a[:])
print(a)

# Petla for
#        0   1   2   3   4   5   6   7   8   9
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while i < len(lista): # UWAGA! < a nie <=
    print(lista[i])
    i += 1

# x to nazwa zmiennej, w której python bedzie wkładał kolejne elementy z listy,
# można ją nazwać dowolnie
for x in lista:
    print(x)

print("-"*30)
# for z użyciem range()
# range(stop) -> liczby od 0 do stop-1
# range(start, stop) -> liczby od start do stop-1
# range(start, stop, krok) -> liczby od start do stop-1 co krok
for x in range(10):
    print(x)

print()

for x in range(4, 10):
    print(x)

print()

for x in range(4, 10, 2):
    print(x)


a = 1
b = 2
print(a, b)

# tmp = a
# a = b
# b = tmp

a, b = b, a

print(a, b)

# ==== NAPISY ====

napis = "Ala ma kota a kot ma kompilator"

# operator dostępu / wycinania dziala tak samo
# jak w przypadku tupli czy list
print(napis[0])
print(napis[1:3]) #lewostronnie domkniety, prawostronnie otwarty
print(napis[4:])
print(napis[::-1])

print(napis.lower())
print(napis.upper())
print(napis.title()) # każda litera słowa z dużej litery
print(napis.capitalize()) # pierwsza litera w napisie z duzej litery

print(napis.split()) # standardowo jest robiony po spacji
print(napis.split('a'))

po_podziale = napis.split()
print(po_podziale)
po_scaleniu = '<->'.join(po_podziale)
print(po_scaleniu)

print(napis.count('a'))
print(napis.index('a')) # pierwszy index w napisie, gdzie wystepuje dany znak
print(napis.find('a'))  # pierwszy index w napisie, gdzie wystepuje dany znak

# print(napis.index('z')) # jak nie znajdzie to rzuci wyjątkiem
print(napis.find('z')) # jak nie znajdzie to zwróci -1

# Palindrom - https://pl.wikipedia.org/wiki/Palindrom
napis = "Ala ma kota" # nie jest palindromem
napis = "Kamil Ślimak" # jest palindromem
napis = napis.lower()
napis = napis.replace(' ', '')
print(napis)
print(napis[::-1])

print(napis == napis[::-1])

print("="*60)
# ==== SLOWNIK ====

slownik = {
    'ala': 10,
    'ela': 20,
    'ula': 30,
    1: 'kot', # -> __hash__ = 1
    2.5: 1500,
    True: 5000, # -> __hash__ = 1
    (1,2): 6000,
    # [1,2]: 7000, # TypeError: unhashable type: 'list' -> lista nie ma zaimplementowanej metody __hash__
}

print(slownik)
print(slownik['ela'])
print(slownik[1])
print(slownik[2.5])
print(slownik[True])

print( (1,2).__hash__() )
print( 'ala'.__hash__())
zmienna = 1
print( zmienna.__hash__() )
print( True.__hash__() )

# print( [1,2].__hash__() )

slownik['ela'] = 1234
print(slownik)


# mozemy sprawdzic czy klucz znajduje się w danym słowniku
print( 'ala' in slownik )
print( 'krysia' in slownik )

# inny sposob na pobieranie elementow
print( slownik.get('ala') )
print( slownik.get('krysia', 123) )

# jak usuwamy elementy ze slownika
print(slownik)
del(slownik['ala'])
print(slownik)

# pobieranie i usuwanie elementu ze słownika, za jednym razem
wartosc = slownik.pop('ela')
print(wartosc)
print(slownik)

print()

# popitem oddaje i usuwa ze slownika ostatnio dodany element
# od Pythona 3.7 - to jest ostatnio dodany element
# wcześniej był to losowy element, nie koniecznie musiał to być ostatni element
wartosc = slownik.popitem()
print(wartosc)
print(slownik)

print("="*60)

# Iterowanie po słowniku przy użyciu for
for x in slownik: # pod x znajduje sie klucz ze slownika
    print(x, " | ", slownik[x])

print("="*60)
for x in slownik.keys():
    print(x)

print("="*60)
for x in slownik.values():
    print(x)

print("="*60)
print(slownik.keys())
print(slownik.values())
print(slownik.items())

print("="*60)

a, b = (10, 20)
print(a)
print(b)

print("="*60)

# zmienne w pętli - klucz i wartosc, moga sie nazywac dowolnie
for klucz, wartosc in slownik.items():
    print(klucz, '->', wartosc)

print("="*60)
# ==== ZBIOR ====

zbior = {10, 20, 30, 40, 50}
print(zbior)

# dodawanie elementu do zbioru
zbior.add(60)
print(zbior)

# usuwanie elementu ze zbioru
zbior.remove(60)
print(zbior)
# zbior.remove(60) # jezeli chcemy usunac element, ktorego nie ma, to remove rzuci wyjatkiem
zbior.discard(60) # jak element jest w zbiorze, to zostanie usuniety, jak go nie ma, to nic sie nie stanie, nie bedzie wyjatku

# print( zbior[0] ) # zbior nie obsluguje dostepu do pojedynczego elementu

for element in zbior:
    print(element)

print( len(zbior) )

# Operacje teoriomnogościowe
a = {1, 2, 3}
b = {1, 2, 4, 5}

# suma, unia, czyli połączenie dwóch zbiorów
print( a | b ) # operator |
print( a.union(b) ) # metoda .union

# część wspólna dwóch zbiorów, iloczyn
print( a & b )
print( a.intersection(b) )

# różnica dwóch zbiorów
print( a - b ) # od zbioru a odejmujemy elementy ze zbioru b
print( a.difference(b) )

# różnica symetryczna - od sumy zbiorow a i b odejmujemy czesc wspolna zbiorow a i b
# dostajemy te elementy zbiorow a i b, ktore nie sa wspolne
print( a ^ b )
print( a.symmetric_difference(b) )

# czy zbiory a i b są rozłączne, czyli czy nie mają wspólnych elementów
print( a.isdisjoint(b) )

# czy a jest podzbiorem b?
print( a <= b ) # zbior a może być taki sam jak zbiór b, bo mamy mniejsze lub równe
print( a < b ) # tutaj zbiory nie mogą być równe

c = {1, 2}
d = {1, 2}

print(c <= d) # True
print(c < d) # False
print(c < a) # True

# można to sprawdzać w drugą stronę, czyli
# sprawdzamy czy a jest nadzbiorem b
print( a > b ) # False
print( a >= b ) # False
print( a > c ) # True
print( a >= c ) # True

# dotychczasowe operacje na zbiorach, ktore wykonywalismy
# powodowaly utworzenie nowego zbioru bedacego wynikiem konretnej operacji

# poznanymi dotychczas operacjami mozemy modyfikowac zbiory
a = {1, 2, 3}
b = {1, 2, 4, 5}

# suma
# a |= b
a.update(b)
print(a) # w zbiorze a zostala zapisana suma zbiorow a i b

# iloczyn, czesc wspolna
a = {1, 2, 3}
b = {1, 2, 4, 5}
# a &= b
a.intersection_update(b) # metody z _update na koncu modyfikuja pierwotny zbior
print(a)

# róznica zbiorów
a = {1, 2, 3}
b = {1, 2, 4, 5}
a -= b
print(a)

# roznica symetryczna
a = {1, 2, 3}
b = {1, 2, 4, 5}
# a ^= b
a.symmetric_difference_update(b)
print(a)
print("="*60)
# ==== WYRAZENIA LISTOWE ====
# mogą być i wyrażenia zbiorowe, wyrażenia słownikowe
# list comprehension, dict comprehension, set comprehension


dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

wynik = []
for wartosc in dane:
    wynik.append( wartosc ** 2 )

print(wynik)

# zrobienie tego samego ale przy uzyciu list comprehension
wynik = [ wartosc ** 2 for wartosc in dane ]
print(wynik)

liczby = { x for x in range(0, 101, 2) } # set comprehension
print(liczby)

print("="*60)

pensje = [1000, 2000, 2500, 1500, 5000]
print(pensje)
# na podstawie pensji policzyc kwote do wypłaty dla pracownika,
# czyli trzeba potracic podatek
do_wyplaty = []
for pensja in pensje:
    do_wyplaty.append( round(pensja * 0.81, 2) )

print(do_wyplaty)

do_wyplaty = [ round(pensja * 0.81, 2) for pensja in pensje ]
print(do_wyplaty)

# Premie -> jeżeli pensja jest mniejsza/rowna 2000 to dajemy 10%, jak wieksza to 0
premie = []
for pensja in pensje:
    if pensja <= 2000:
        premie.append(0.10)
    else:
        premie.append(0)

print(premie)

premie = [ 0.10 if pensja <= 2000 else 0 for pensja in pensje ]
print(premie)

# wartosc premii
print( list( zip(do_wyplaty, premie) ) )

wartosc_premii = [ pensja * premia for pensja, premia in zip(do_wyplaty, premie) ]
print(wartosc_premii)

# policzyć kwoty do wypłaty, czyli kwota_netto + wartość premii
do_wyplaty_z_premia = [ kwota_do_wyplaty + kwota_premii for kwota_do_wyplaty, kwota_premii in zip(do_wyplaty, wartosc_premii)]
print(do_wyplaty_z_premia)

# potrzebuje liste pracownikow co im trzeba wyplacic wiecej niz 2000 zł
pracownicy_drozsi = []
for pensja in do_wyplaty_z_premia:
    if pensja > 2000:
        pracownicy_drozsi.append(pensja)

print(pracownicy_drozsi)

pracownicy_drozsi = [ pensja for pensja in do_wyplaty_z_premia if pensja > 2000 ]
print(pracownicy_drozsi)

# przyklady - podsumowanie
a = [ x for x in range(0,11) ] # list comprehension
print(type(a))
print(a)

a = { x for x in range(0,11) } # set comprehension
print(type(a))
print(a)

a = { x: x+1 for x in range(0,11) } # dict comprehension - muszę podać klucz i wartość
print(type(a))
print(a)

# nie ma tuple comprehension
# ale możemy w tej manierze użyć nawiasów ( )
# i wtedy dostaniemy generator expression

generator = ( x for x in range(0, 11) )
print(generator)

for liczba in generator:
    print(liczba)