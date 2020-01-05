import turtle

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


bogdan = turtle.Turtle()

for x in liczby_pierwsze():
    bogdan.forward(x)
    bogdan.right(90)

turtle.done()