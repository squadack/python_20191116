class MojWyjatek(Exception):
    pass

def niebezpieczna_operacja(x):
    if x == 3:
        raise ValueError("No się zepsuło...")
    if x == 6:
        raise MojWyjatek("moj wyjatek")
    print("Operacja zakonczona sukcesem.")

x = 6
y = 4

try:
    wynik = x / y
    print(wynik)
    niebezpieczna_operacja(6)
except ZeroDivisionError:
    print("Nie dziel przez 0!")
except ValueError as e:
    print(f"BŁĄD: {e}")
    # raise
except MojWyjatek:
    print("Zlapalem moj wyjatek")
finally:
    print("wykona sie zawsze")

print("koniec programu")
