"""
Napisz program wyświetlający minimalną oraz maksymalną liczbę z
wszystkich liczb wprowadzonych przez użytkownika. Daj
użytkownikowi możliwość zakończenia wprowadzania liczb
odpowiednią komendą. Zadbaj o obsłużenie przypadku gdy
użytkownik nie wprowadzi żadnej liczby.
"""


# petla
    # pytam uzytkownika o liczbe
        # zwykla liczba
            # sprawdzam czy wieksze/mniejsze niz to co mam do tej pory
        # komenda koniec - kończe petle

minimum = None
maximum = None

while True:
    dane_wejsciowe = input("Podaj liczbę: ")

    if dane_wejsciowe == 'koniec':
        break # kończy działanie ifa i pętli

    if dane_wejsciowe.lstrip('-').isdecimal() is False:
        print("Niepoprawna liczba!")
        continue

    liczba = int(dane_wejsciowe)

    if minimum is None or liczba < minimum:
        minimum = liczba

    if maximum is None or liczba > maximum:
        maximum = liczba


if minimum is None or maximum is None:
    print('Nie podałeś żadnej liczby ;D   ')
else:
    print(f'Znalezione minimum = {minimum} i maximum = {maximum}')




