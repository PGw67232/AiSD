r = int(input("podaj wielkosc tablicy: "))


def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)


F = [fib(n) for n in range(r)]
print(F)
