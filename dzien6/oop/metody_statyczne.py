class Klasa:
    def metoda(self):
        print("zwykła metoda")

    @staticmethod
    def metoda_statyczna():
        print("metoda statyczna")

    @classmethod
    def metoda_klasowa(cls):
        print("metoda klasowa")
        return cls()

class InnaKlasa(Klasa):
    pass


x = InnaKlasa.metoda_klasowa()
print(type(x))
Klasa.metoda_statyczna()
k = Klasa()
k.metoda()
k.metoda_statyczna()