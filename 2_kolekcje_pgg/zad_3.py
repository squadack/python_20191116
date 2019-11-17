"""
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w
zadanej liście liczb całkowitych.
"""

liczby = [1, 2, 3, -100, -10, 0, 4]

liczba_dodatnich = 0
liczba_ujemnych = 0

for element in liczby:
    if element > 0:
        liczba_dodatnich += 1
    elif element < 0:
        liczba_ujemnych += 1

print(f'Ujemnych: {liczba_ujemnych} dodatnich: {liczba_dodatnich}')

