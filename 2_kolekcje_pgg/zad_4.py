"""
Napisz program wypisujący wszystkie libczy od 0 do 100, podzielne
przez 3 lub podzielne przez 5. Wypisz także jak dużo takich liczb
wystąpiło w tym przedziale.
Liczby podzielne przez 3 lub 5:
0
3
5
...
96
99
100
W przedziale 0-100 jest 48 liczb podzielnych przez
3 lub 5
"""
ile = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile += 1

print(f'Wystapilo {ile} takich liczb.')




