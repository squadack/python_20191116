"""
https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
https://artblot.files.wordpress.com/2013/05/fibonacci-rabbits.png
Złożoność O(2^n)
n = 0 -> 0
n = 1 -> 1
n > 1 -> f(n-1)+f(n-2)

f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 5
f(6) = 8
...
"""

def fib(n: int) -> int:
    if n < 0:
        raise ValueError('n musi byc wieksze od 0')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

import pytest
def test_n_ujemne():
    with pytest.raises(ValueError):
        fib(-1)

def test_fibonacci():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(10) == 55
    assert fib(15) == 610





