"""
Napisz program zamieniający miejscami w zadanej liście liczb
element największy z najmniejszym.
"""

liczby = [49, 50, 20, 40, 35, 10]
#        [49, 10, 20, 40, 35, 50]

indeks_min = None
indeks_max = None

for indeks, wartosc in enumerate(liczby):
    if indeks_min is None or wartosc < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or wartosc > liczby[indeks_max]:
        indeks_max = indeks


liczby[indeks_min], liczby[indeks_max] = liczby[indeks_max], liczby[indeks_min]

print(liczby)
