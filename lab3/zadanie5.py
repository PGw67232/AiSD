def hanoi(x, A, B, C):
    if x == 1:
        print("1 z", A, ": ", B)
        return
    else:
        hanoi(x-1, A, C, B)
        print(x, " z ", A, " : ",B)
        hanoi(x-1, C, B, A)

x = int(input("Podaj ilosc krazkow: "))
print("Wymagane ruchy: ")
print(hanoi(x,"A", "C", "B"))
