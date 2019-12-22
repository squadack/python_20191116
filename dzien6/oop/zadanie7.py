class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.przepracowany_czas = 0

    def register_time(self, ile):
        self.przepracowany_czas += ile
        if ile > 8:
            self.przepracowany_czas += ile - 8

    # zwraca wyplate
    def pay_salary(self):
        wyplata = self.przepracowany_czas * self.stawka
        self.przepracowany_czas = 0
        return wyplata

class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        bonus = self.bonus
        self.bonus = 0
        return super().pay_salary() + bonus

p = PremiumEmployee("Jan", "Kowalski", 100)
p.register_time(5)
p.give_bonus(1000)
print(p.pay_salary())
print(p.pay_salary())
