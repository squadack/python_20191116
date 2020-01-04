def tournament(lista):
    for g1 in lista:
        for g2 in lista:
            if g1 != g2:
                yield g1, g2

# wszystkie pary BEZ rewanży
def tournament2(lista):
    for i1 in range(len(lista)):
        for i2 in range(i1 + 1, len(lista)):
            yield lista[i1], lista[i2]


for gracz_1, gracz_2 in tournament2(['A', 'B', 'C']):
    print(f"{gracz_1} vs. {gracz_2}")