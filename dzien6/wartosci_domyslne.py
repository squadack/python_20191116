def fun2(x=None):
    if x is None:
        x = []
    x.append(345)
    print(x)

fun2()
fun2()
fun2()
fun2()
fun2()

def fun(x=[]):
    x.append(123)
    print(x)
lista = []
fun(lista)
print(lista)
print("--------")
fun()
fun()
fun()

def foo(x=input("Podaj wartosc:")):
    print(x)
print("----")
foo()
foo()
