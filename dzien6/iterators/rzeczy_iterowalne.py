# x = [1,2,3]
# for i in x:
#     print(i)

# it = iter(x)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break

class Licznik:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.i = self.limit
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration
        wynik = self.i
        self.i -= 1
        return wynik

x = Licznik(3)
for i in x:
    print(i)
