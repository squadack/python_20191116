class Klasa:
    POLE_KLASOWE = 100

    def __init__(self, x):
        self.x = x

k = Klasa(5)
p = Klasa(10)
print(k.x)
print(p.x)
print(Klasa.POLE_KLASOWE)
Klasa.POLE_KLASOWE = 2
print(Klasa.POLE_KLASOWE)
print(k.POLE_KLASOWE)