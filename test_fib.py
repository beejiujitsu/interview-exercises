from fib import fib

def test_five():
    assert list(fib(5)) == 3

def test_twenty():
    assert list(fib(20)) == 5