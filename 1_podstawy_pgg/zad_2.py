"""
Korzystając z przypisywania wartości do zmiennych, napisz program
obliczający pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5.
"""

# nazwa_zmiennej = wartosc
# = -> operator przypisania
podstawa_a = 3 # python tworzy zmienna podstawa_a i wklada do niej wartosc 3
podstawa_b = 9
wysokosc = 6.5

# możemy do zmiennej przypisywać WYNIK wyrażeń złożonych
# takiej konwencji się nie zaleca, ona działa, ale nie jest zalecana
# tak się robi w Javie, ale nie w Pythonie
poleTrapezu = 1 / 2 * (podstawa_a + podstawa_b) * wysokosc

print(poleTrapezu)