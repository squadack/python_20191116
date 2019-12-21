class Samochod:
    def __init__(self, marka):
        print("UWAGA, tworze samochod")
        self.marka = marka

    def inicjuj(self, marka):
        self.marka = marka

    def jedz(self):
        print(f"{self.marka}: brum brum")

print("start")
x = Samochod("Skoda")
y = Samochod("Audi")
print("samochod stworzony")
x.jedz()
y.jedz()