class Product:
    NASTEPNE_ID = 1
    def __init__(self, nazwa, cena):
        self.id = Product.NASTEPNE_ID
        Product.NASTEPNE_ID += 1
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

    def __str__(self):
        return f"Nazwa: {self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN"

    def __repr__(self):
        return f"<Product ID: {self.id}>"

x = [Product("Woda", 10) for _ in range(100)]
print(x)
print(Product.NASTEPNE_ID)