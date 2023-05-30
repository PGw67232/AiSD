r = int(input("podaj wielkosc tablicy: "))


def fib(i, j):
    if j in {0, 1}:
        return j
    return fib(j - 1) + fib(j - 2)


F = [fib(j) for j in range(j)]
print(F)