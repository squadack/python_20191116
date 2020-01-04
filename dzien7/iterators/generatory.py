def generator():
    yield 3
    yield 5
    yield 7

def nasz_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

def nasz_range2(x):
    for i in range(x):
        yield i

for i in nasz_range2(5):
    print(i)

def poczta():
    i = 0
    while True:
        yield i
        i += 1
        i %= 10

# for i in poczta():
#     print(i)

# print(generator())
# for i in generator():
    # print(i)

# it = iter(generator())
# print(next(it))
# print(next(it))
# print(next(it))