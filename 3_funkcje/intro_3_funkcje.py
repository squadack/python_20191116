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