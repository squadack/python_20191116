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

print("="*60)
# ==================================

# UWAGA! ACHTUNG! ATTENTION!
# funkcja to kolejny typ danych
# funckję mogę przekladac miedzy roznymi pudelkami (zmiennymi)
def czesc(imie):
    print(f"Czesc {imie}")

czesc('Piotr')

funkcja_co_mowi_czesc = czesc
funkcja_co_mowi_czesc('Zosia')

moj_print = print
moj_print('Ala ma kota')



def kwadrat(x):
    return x ** 2

print(kwadrat(3))


kwadrat = lambda x: x ** 2
print(kwadrat(4))

square = kwadrat
print(square(5))


def sumator(a, b, c):
    return a + b + c

print(sumator(10, 20, 30))

# w funkcji lambda możemy definiować wiele argumentów
sumator = lambda a, b, c: a + b + c
print(sumator(10, 20, 30))

# zwracanie rzeczy z funkcji lambda
def x_mniejsze_od_y(x, y):
    if x < y:
        return True
    else:
        return False

print( x_mniejsze_od_y(2, 3) )
print( x_mniejsze_od_y(20, 10) )

x_mniejsze_od_y = lambda x, y: x < y
print( x_mniejsze_od_y(2, 3) )
print( x_mniejsze_od_y(20, 10) )

# zwracanie ustalonych wartosci
def witaj_swiecie():
    return "Hello world!"

print(witaj_swiecie())

# lambda bez żadnych parametrów
witaj_swiecie = lambda : "Hello world!"
print(witaj_swiecie())

# funkcji lambda bardzo często używa się wewnątrz innych funkcji,
# tzn. przekazujemy funkcję lambda jako argument innej funkcji, żeby wykorzystać ją w środku

def wykonaj_operacje_na_liscie(lista, operacja):
    rezultat = []

    for element in lista:
        rezultat.append( operacja(element) )

    return rezultat

# moja_operacja = lambda x: x ** 2
wynik = wykonaj_operacje_na_liscie([10, 20, 30], lambda x: x ** 2) # tutaj funckja służy do dostarczenia/przerobienia danych
print(wynik)


# funkcja w pythonie map(), która robi bardzo podobną rzecz co wykonaj_operacje_na_liscie
lista = [10, 20, 30, 40]
print( list(map(lambda x: x*2, lista)) )

# filter
lista = [-1, 2, -15, -81, 40, 100]
print( list( filter(lambda x: x > 0, lista) ) )

# sortowanie
lista = [9, 8, 5, 2, 6, 1]
print(lista)
# lista.sort() # sortuje w porządku rosnącym
lista.sort(reverse=True) # sortuje w porządku malejącym
print(lista)

lista = [ (2, 2), (3, 4), (4, 1), (1, 3) ]
print(lista)
lista.sort()
lista.sort(key=lambda x: x[1])
print(lista)
print()



lista = [ (2, 2), (3, 4), (4, 1), (1, 3) ]


def komparator(a, b):
    """
    Komparator ma zwrócić dla dwóch porównywanych elementów następujace wartości,
    których użyje metoda sort do sortowania.
    -1 - kiedy a powinno być przed b ("a jest mniejsze od b")
    0  - kiedy a i b są "rowne"
    1  - kiedy a jest większe od b, a powinno być po b
    :param a:
    :param b:
    :return:
    """
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1


from functools import cmp_to_key

print(lista)
lista.sort(key=cmp_to_key(komparator))
print(lista)


