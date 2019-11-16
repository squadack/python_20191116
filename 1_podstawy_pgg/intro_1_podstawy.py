print('Hello World!')

# komentarz do końca linijki

# TYPY DANYCH

# NAPISY, ciągi znaków, tzw. stringi
# definiujemy w ' lub "
print('Ala ma kota')
print("Ala ma kota")

# LICZBY CAŁKOWITE, int (od integer)
# int są nieograniczone, tzn. dowolnie duże (małe) liczby mogę przechowywać
print(10)
print(-8)

# LICZBY ZMIENNOPRZECINKOWE - float
# float w pythonie jest zaimplementowany poprzez typ double w C
import sys
print(sys.float_info)

print(3.5) # uwaga! kropka, nie przecinek
print(3.0)
print(-1.5)
print(1.0)
print(1.)
print(0.1)
print(.1)

print(type(1))
print(type(1.0))

# BOOL, boolean, typ boolowski
# przyjmuje dwie wartości: True, False
print(True)
print(False)
print(type(True))

# NONE, null, wartość oznaczająca brak wartości
print(None)

# True, False, None - muszą być pisane z dużej litery

# OPERATORY
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) # dzielenie całkowitoliczbowe
print(10 % 3) # reszta z dzielenia, dzielenie modulo
print(10 ** 3) # potęgowanie

print("Ala" + "ma kota") # konkatenacja
print("Ala" * 10)
# print("Ala" * "kot")

print(type(10))
print(type(10.0))
print(type("10"))

print('ala ma \'kota\' a kot ma kompilator')
print("ala ma \"kota\" a kot ma kompilator")
print('ala ma "kota" a kot ma kompilator')
print("ala ma 'kota' a kot ma kompilator")

# definiowanie stringów na wiele linijek
# ' i " pozwalają definiować napisy w jednej linijce
# ''' i """ pozwalają definiować napisy w wielu linijkach
print('''
ala
ma 
kota
''')
print("""
Kot
ma 
kompilator
""")

print()
print(1 == 1) # Uwaga!!!! na dwa znaki =
print(1 != 1)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)





