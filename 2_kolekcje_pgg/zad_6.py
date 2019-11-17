"""
Napisz program zamieniający miejscami w zadanej liście liczb
element największy z najmniejszym.
"""

liczby = [49, 50, 20, 40, 35, 10]
#        [49, 10, 20, 40, 35, 50]

liczby_kopia = list(liczby) # kopia bo sortowanie listy ja zmienia (sortuje)
liczby_kopia.sort()

print(liczby)
print(liczby_kopia)

wartosc_minimalna = liczby_kopia[0]
wartosc_maksymalna = liczby_kopia[-1]

klucz_wartosci_minimalnej = liczby.index(wartosc_minimalna)
klucz_wartosci_maksymalnej = liczby.index(wartosc_maksymalna)
print(klucz_wartosci_minimalnej)
print(klucz_wartosci_maksymalnej)

# tmp = liczby[klucz_wartosci_minimalnej]
# liczby[klucz_wartosci_minimalnej] = liczby[klucz_wartosci_maksymalnej]
# liczby[klucz_wartosci_maksymalnej] = tmp

liczby[klucz_wartosci_minimalnej], liczby[klucz_wartosci_maksymalnej] = liczby[klucz_wartosci_maksymalnej], liczby[klucz_wartosci_minimalnej]

print(liczby)