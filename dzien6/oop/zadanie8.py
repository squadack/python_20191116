class CashMachineException(Exception):
    pass

class CashMachine:
    def __init__(self, limit=5):
        self.__zawartosc = []
        self.limit = limit

    def is_available(self):
        return len(self.__zawartosc) > 0

    def put_money(self, banknoty):
        if len(self.__zawartosc) + len(banknoty) > self.limit:
            raise CashMachineException("Brak miejsca w bankomacie!")
        self.__zawartosc.extend(banknoty)

    def withdraw_money(self, ile):
        if ile % 10 != 0:
            raise CashMachineException(f"Kwota nie jest podzielna przez 10!")
        kwota = ile
        wynik = []
        for b in self.__zawartosc:
            if b <= ile:
                wynik.append(b)
                ile -= b
        if ile != 0:
            raise CashMachineException(f"Brak odpowiednich banknotów do wyplacenia kwoty {kwota}")
        for b in wynik:
            self.__zawartosc.remove(b)
        return wynik


bankomat = CashMachine()
while True:
    op = input("Podaj rodzaj operacji [WPLATA, WYPLATA, KONIEC]:")
    if op == "KONIEC":
        break
    elif op == "WYPLATA":
        try:
            kwota = int(input("Podaj kwote do wyplacenia: "))
            print(bankomat.withdraw_money(kwota))
        except CashMachineException as e:
            print(f"BŁĄD: {e}")
        except ValueError:
            print("Podaj liczbę!")
    elif op == "WPLATA":
        try:
            lista = input("Podaj banknoty oddzielone spacjami:").split(" ")
            bankomat.put_money(list(map(int, lista)))
        except CashMachineException as e:
            print(f"BŁĄD: {e}")
