"""
W sesji interaktywnego środowiska interpretera stwórz tuplę
zawierającą 10 różnych liczb całkowitych. Korzystając z operatora
dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie)
- co trzeci element
- co drugi element licząc od końca
"""

#    0   1   2   3   4   5   6   7   8   9 -> klucze
a = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#    1   2   3   4   5   6   7   8   9   10 -> który element

print( a[1] ) # drugi element
print( a[-2] ) # przedostatni element
print( a[2:7] ) # elementy od trzeciego do siódmego (włącznie)
print( a[::3] ) # co trzeci element
print( a[::-2] ) # co drugi element licząc od końca

