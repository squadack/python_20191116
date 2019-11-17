"""
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej
planszy o rozmiarach 10 na 10. Użytkownik może wprowadzać
komendy zmieniające położenie postaci. Po każdym ruchu
użytkownik powinien otrzymywać informację o tym, czy zmierza
dobrym kierunku. Wyjście poza planszę oznacza koniec gry. Po
znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez
użytkownika na dojście do celu.
Dodatkowo:
I po wykonaniu większej liczby kroków niż dwukrotność
minimalnej liczby kroków umieść skarb w nowym miejscu,
I z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki
po wykonaniu kroku.
"""

gracz_x = 1
gracz_y = 1

skarb_x = 5
skarb_y = 5

while True:
    print(f'Twoja pozycja x={gracz_x:2} y={gracz_y:2}')

    kierunek = input("Podaj kierunek (w,s,a,d): ")

    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print("Niepoprawny kierunek")
        continue

    if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
        print("Jesteś poza planszą. Koniec gry!")
        break






