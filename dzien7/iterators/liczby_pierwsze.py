def czy_pierwsza(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def liczby_pierwsze():
    num = 1
    while True:
        if czy_pierwsza(num):
            yield num
        num += 1

for i, x in enumerate(liczby_pierwsze(), 1):
    # if x >= 100:
    #     break
    print(f"{i}: {x}")