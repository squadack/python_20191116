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

    @classmethod
    def with_products(cls, lista_produktow):
        koszyk = cls()
        for prod in lista_produktow:
            koszyk.add_product(prod)
        return koszyk

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

class Kontener(Basket):
    def zaladuj_na_statek(self):
        print("Ładuje kontener na statek")

k = Kontener.with_products([Product(1, "W", 10), Product(2, "M", 100)])
print(k.count_total_price())
k.zaladuj_na_statek()