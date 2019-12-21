class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1)
print(v2)
v3 = v1 + v2 # v3 = v1.__add__(v2)
print(v3)
print(f"{v1} + {v2} = {v1 + v2}")
# v1 < v2 # v1.__lt__(v2)
# v2 == v2 # v1.__eq__(v2)
# v1 * 3
# 3 * v1