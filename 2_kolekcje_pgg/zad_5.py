"""
Napisz program wypisujący na konsolę tabliczkę mnożenia dla liczb
od 1 do 10 w postaci tabelki.
"""

for a in range(1, 11):
    for b in range(1, 11):
        print(f'{a*b:3} ', end='')
    print()

