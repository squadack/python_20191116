class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other): # self * other
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other): # other * self
        return self * other

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __lt__(self, other): # self < other
        return self.length() < other.length()

    def __eq__(self, other): # self == other
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1)
print(v2)
v3 = 5 * v1
print(v3)
if v1 < v2:
    print("v1 mniejsze")
if v1 == Vector(1, 2):
    print("TAK")
# a * b # a.__mul__(b) | b.__rmul__(a)
# print(f"{v1} - {v2} = {v1 - v2}")
# v1 < v2 # v1.__lt__(v2)
# v2 == v2 # v1.__eq__(v2)
# v1 * 3
# 3 * v1