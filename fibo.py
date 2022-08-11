def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib2(n):
    reslt = []
    a, b = 0, 1
    while b < n:
        reslt.append(b)
        a, b = b, a + b
    return reslt

a = 40
