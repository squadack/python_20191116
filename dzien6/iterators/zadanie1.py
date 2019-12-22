class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i > self.limit:
            raise StopIteration
        wynik = self.i
        self.i += 1
        return wynik


for i in Counter(30):
    print(i)