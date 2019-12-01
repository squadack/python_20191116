# ==== FUNKCJE =====
def powiedz_czesc():
    print("Cześć!")

powiedz_czesc()
powiedz_czesc()
powiedz_czesc()

def powiedz_czesc_komus(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')

powiedz_czesc_komus("Piotr", "GG")
powiedz_czesc_komus("Krysia", "Nowak")

# te dwie funkcje (powiedz_czesc, powiedz_czesc_komus) nic nie zwracaja
# mają "efekt uboczny", tzn. taki, że coś zostanie wypisane na konsolę
# funkcje mogą zwracać wartości, to znaczy możemy zwrócić jakąś wartość, która
# będzie wynikiem działania mojej funkcji

def suma(a, b):
    return a + b # return powoduje zwrócenie jakiejś wartości z funkcji
    print('ala ma kota') # ta instrukcja sie NIE uruchomi, bo jest po returnie!

wynik = suma(2, 3)
print(wynik)

# docstring
# type hinting - sugerowanie typów argumentów
def iloczyn(a: int, b: int) -> int:
    """
    To jest docstring. Mowi, co dana funkcja robi. Jest to element dokumentacji
    Funkcja przyjmuje dwa inty i zwraca int
    :param a:
    :param b:
    :return:
    """
    return a * b


wynik = iloczyn(2, 3)
print(wynik)

wynik = iloczyn(2.5, 3.5)
print(wynik)

print("="*60)
# ============
napis = 'ala ma kota'
print( napis.count('a') )


################################################

print('ala', 'krysia', 'zosia')
print('a')
print('b')
print('c')

print('tomek', end='|')
print('piotrek')

# ==== Argumenty domyślne w funkcjach =====
def opakowywacz(napis, start='>', end='<'):
    return start + napis + end

# uruchamianie funkcji z przekazanie argumentów w sposób pozycyjny
print( opakowywacz('ala ma kota', '>>>', '<<<') )
print( opakowywacz('kot ma kompilator')) # start i end maja tutaj wartości domyślne, nie musze ich podawać
print( opakowywacz('ala ma kota', '>>>') )

# uruchamianie funkcji odbywa się poprzez przekazanie argumentów nazwanych
print( opakowywacz(start='>>', end='<<', napis='ala ma kota') )
print( opakowywacz(napis='ala ma kota')) # start i end mają wartość domyślną

# uruchamianie funkcji z przekazaniem argumentów w sposób pozycyjny i nazwany
print( opakowywacz('ala na kota', end='---', start='>>>') )

# jak mieszamy dwa sposoby, to najpierw podajemy argumenty pozycyjne, później nazwane
# print( opakowywacz(end="<<<", 'ala ma kota') )


# ======= Dowolnie wiele argumentów =======
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("="*60)

def zliczacz(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
    print()

# bez argumentów
zliczacz()

# tylko argumenty pozycyje
zliczacz(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tylko argumenty nazwane
zliczacz(a=1, b=2, c='ala', d=4.5, e=True)

# argumenty pozycyjne i nazwane - wymieszane
zliczacz(1, 2, 3, a=1, b=2, c=True)

# argumenty pozycyjne, z wartoscia domyslna, *args, **kwargs można mieszać
def fun(a, b, c=10, *args, **kwargs):
    print(a, b, c, args, kwargs)

fun(1, 2)
fun(1, 2, 3, 4, 5, 6, 7)
fun(1, 2, 3, 4, 5, 6, 7, x=1, y=1)
