class Vowels:
    def __init__(self, napis):
        self.napis = napis

    # iter zwraca iterator (czyli cos co ma metode __next__())
    def __iter__(self):
        self.indeks = 0
        return self

    # kolejne wywolania next zwracają kolejne interesujące nas elementy
    # jesli nie ma nastepnego elementu to podnosimy wyjątek StopIteration
    def __next__(self):
        while self.indeks < len(self.napis):
            znak = self.napis[self.indeks]
            self.indeks += 1
            if znak.lower() in "aeiouy":
                return znak
        raise StopIteration

for x in Vowels("Ala ma kota"):
    print(f" - {x}")
