class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

x = Product(1, "Woda", 10.99)
y = Product(2, "Banan", 3.98)
x.print_info()
y.print_info()