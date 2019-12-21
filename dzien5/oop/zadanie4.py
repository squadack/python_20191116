class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

class Basket:
    def __init__(self):
        self.zawartosc = []

    def add_product(self, p: Product, ilosc: int):
        self.zawartosc.append(p)

    def count_total_price(self):
        # return sum(p.cena for p in self.zawartosc)
        suma = 0
        for produkt in self.zawartosc:
            suma += produkt.cena
        return suma

p1 = Product(1, "Woda", 10.99)
p2 = Product(2, "Cola", 5.99)
b = Basket()
b.add_product(p1)
b.add_product(p2)
b.add_product(Product(3, "Cokolwiek", 100))
print(b.count_total_price())
