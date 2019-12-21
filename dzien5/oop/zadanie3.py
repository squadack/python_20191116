class Car:
    def __init__(self, zasieg):
        self.zasieg = zasieg
        self.max_zasieg = zasieg

    def drive(self, dystans):
        if dystans <= self.zasieg:
            self.zasieg -= dystans
            return dystans
        else:
            wynik = self.zasieg
            self.zasieg = 0
            return wynik

    def charge(self):
        self.zasieg = self.max_zasieg

    def stan_paliwa(self):
        print(f"{self.zasieg}/{self.max_zasieg}km")

c = Car(100)
print(c.drive(70))
c.stan_paliwa()
print(c.drive(50))
print(c.drive(50))
c.charge()
print(c.drive(50))
