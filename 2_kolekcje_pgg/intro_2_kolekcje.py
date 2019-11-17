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