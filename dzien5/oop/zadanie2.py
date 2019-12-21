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

    def pay_salary(self):
        wyplata = self.przepracowany_czas * self.stawka
        self.przepracowany_czas = 0
        return wyplata

    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie} {self.nazwisko}")

p = Employee("Jan", "Nowak", 100)
p.register_time(5)
p.register_time(5)
print("Wyplata:", p.pay_salary())
p.register_time(10)
print("Wyplata:", p.pay_salary())
print("Wyplata:", p.pay_salary())
p.przedstaw_sie()