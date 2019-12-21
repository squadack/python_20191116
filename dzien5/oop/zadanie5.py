class CashMachine:
    def __init__(self):
        self.__zawartosc = []

    def is_available(self):
        # return bool(self.zawartosc)
        return len(self.__zawartosc) > 0
        # if len(self.zawartosc) > 0:
        #     return True
        # return False

    def put_money(self, banknoty):
        self.__zawartosc.extend(banknoty)
        # for b in banknoty:
        #     self.zawartosc.append(b)

    def withdraw_money(self, ile):
        wynik = []
        for b in self.__zawartosc:
            if b <= ile:
                wynik.append(b)
                ile -= b
        if ile != 0:
            return []

        # usuwamy wszystkie wybrane banknoty z self.zawartosc
        for b in wynik:
            self.__zawartosc.remove(b)
        return wynik

bankomat = CashMachine()
bankomat.put_money([200, 100, 100, 50])
print(bankomat.withdraw_money(150))
print(bankomat.withdraw_money(150))
print(bankomat.withdraw_money(300))

# print(dir(bankomat))
# print(bankomat._CashMachine__zawartosc)


