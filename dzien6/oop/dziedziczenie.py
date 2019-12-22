class Zwierz:
    def __init__(self, imie):
        self.imie = imie

    def jedz(self):
        print(f"{self.imie}: am am")

    def spij(self):
        print(f"{self.imie}: zzzzz")

class Pies(Zwierz):
    def __init__(self, imie, wiek):
        super().__init__(imie)
        self.wiek = wiek

    def szczekaj(self):
        print(f"{self.imie}: hau hau")

    def spij(self):
        print(f"{self.imie}: chrrrr...")

z = Pies("Azor", 4)
z.jedz()
z.spij()
z.szczekaj()

print(isinstance(z, Zwierz))
print(isinstance(z, Pies))
