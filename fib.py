def fib(n, current = 0, last = 0):
    if current in (0, 1):
        yield n
        current = last
        #fib(n )