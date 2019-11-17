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


