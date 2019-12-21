class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

    def __str__(self):
        return f"Nazwa: {self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN"

    def __repr__(self):
        return f"<Product ID: {self.id}>"

class Basket:
    def __init__(self):
        self.zawartosc = []

    def add_product(self, p: Product, ilosc: int = 1):
        for s in self.zawartosc:
            if s["produkt"].id == p.id:
                s["ilosc"] += ilosc
                return
        # jeśli tu dojdziemy to znaczy, ze na liscie nie ma jeszcze takiego produktu
        slownik = {"produkt": p, "ilosc": ilosc}
        self.zawartosc.append(slownik)

    def count_total_price(self):
        suma = 0
        for slow in self.zawartosc:
            suma += slow["produkt"].cena * slow["ilosc"]
        return suma

p1 = Product(1, "Woda", 10.99)
p2 = Product(2, "Cola", 5.99)
b = Basket()
b.add_product(p1)
b.add_product(p2, 15)
b.add_product(p1)
b.add_product(Product(3, "Cokolwiek", 100), 5)
print(b.count_total_price())
print(b.zawartosc)

# print(p1)
# print(str(p1))
# print(p1.__str__())
# print(f"produkt: {p1}")
# print([p1, p1])
# print(repr(p1))