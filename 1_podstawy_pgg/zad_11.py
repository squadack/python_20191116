"""
Napisz program, który na podstawie pozycji gracza (x, y) na
planszy w przedziale od 0 do 100 wyświetli jego przybliżone
położenie (centrum, prawy górny róg, górna krawędź, . . . ) lub
informację o pozycji poza planszą. Przyjmij wartość 10 jako
margines krawędzi.
Przykładowy komunikat programu:
Podaj pozycję gracza X: 95
Podaj pozycję gracza Y: 95
Gracz znajduje się w prawym górnym rogu.
"""

x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

# if x >= 0 and x <= 10: -> if 0 <= x <= 10:
# elif x > 10 and x <= 90: -> elif 10 < x <= 90:

if 0 <= x <= 10:
    if 0 <= y <= 10:
        print("lewy dolny róg")
    elif 10 < y <= 90:
        print("lewy krawędź")
    elif 90 < y <= 100:
        print("lewy górny róg")
    else:
        print("jesteś poza planszą")
elif 10 < x <= 90:
    if 0 <= y <= 10:
        print("lewa krawędź")
    elif 10 < y <= 90:
        print("centrum")
    elif 90 < y <= 100:
        print("góna krawędź")
    else:
        print("jesteś poza planszą")
elif 90 < x <= 100:
    if 0 <= y <= 10:
        print("prawy dolny róg")
    elif 10 < y <= 90:
        print("prawa krawędź")
    elif 90 < y <= 100:
        print("prawy górny róg")
    else:
        print("jesteś poza planszą")
else:
    print("poza planszą")