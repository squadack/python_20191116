"""
Napisz program, który na podstawie wprowadzonych wymiarów
opakowania, obliczy jego objętość oraz sprawdzi, czy jest ona
większa od 1 litra (1000 cm3).
"""

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))

objetosc = x * y * z
# czy_wieksze_od_litra = x * y * z > 1000
# czy_wieksze_od_litra = (x * y * z) > 1000
czy_wieksze_od_litra = objetosc > 1000

print(f'Objetość: {objetosc}')
print(f'Czy większa od 1 litra? {czy_wieksze_od_litra}')

