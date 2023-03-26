lista = [1, 2, 3, 11, 21, 111, 231]


def sor(liczby):
    liczby = sorted(lista)
    roz = [str(x) for x in lista]
    roz = sorted(roz)
    wynik = [int(x) for x in roz]
    return wynik


print(sor(lista))
