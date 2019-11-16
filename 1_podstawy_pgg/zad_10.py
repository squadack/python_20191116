"""
Napisz program, który na podstawie dwóch podanych liczb obliczy
wynik zadanej operacji (dodawanie, odejmowanie, mnożenie,
dzielenie). W przypadku podania nieprawidłowej operacji program
ma wyświetlić odpowiedni komunikat o błędzie.
Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji: +
Wynik: 15
"""

liczba_1 = int(input("Podaj pierwszą liczbę: "))
liczba_2 = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj operację (+, -, *, /): ")

if operacja == '+':
    wynik = liczba_1 + liczba_2
elif operacja == '-':
    wynik = liczba_1 - liczba_2
elif operacja == '*':
    wynik = liczba_1 * liczba_2
elif operacja == '/':
    wynik = liczba_1 / liczba_2
else:
    wynik = None

if wynik == None:
    print("Podałeś niedozwoloną operację!")
else:
    print(f'Wynik {liczba_1}{operacja}{liczba_2} = {wynik}')
