class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return Counter_iterator(self)

class Counter_iterator:
    def __init__(self, counter):
        self.counter = counter
        self.x = 0

    def __next__(self):
        if self.x < self.counter.limit:
            wynik = self.x
            self.x += 1
            return wynik
        raise StopIteration

i = Counter(3)
# i = [0, 1, 2]
for x in i:
    print(f"{x}: ", end="")
    for y in i:
        print(f"{y} ", end="")
    print()
