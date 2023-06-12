# uzytkownik podaje wielkosc listy, n > 0
# elementy listy losowane z przedzialu (x, y) podanego przez uzytkownika
# wyswietlenie listy uporzadkowanej rosnaco
# podanie szukanej liczby
# wyswietlenie czy taka jest lub jej nie ma a jesli jest to podac index
import random


def quicksort(l, r, list):
    if l >= r:
        return

    v = list[r]
    p = l

    for j in range(l, r):
        if list[j] < v:
            list[p], list[j] = list[j], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list


def binarysearch(lista, left, right, szukana):
    left = 0
    right = n - 1
    srodek = (left + right) // 2
    while left <= right:
        srodek = (left + right) // 2
        if lista[srodek] == szukana:
            return srodek
        elif lista[srodek] > szukana:
            right = srodek - 1
        else:
            left = srodek + 1

    return -1


while True:
    n = int(input('podaj wielkosc tabeli: '))
    if n > 0:
        print('okej')
        break
    else:
        print('podaj n wiekrze od 0')

while True:
    x = int(input('podaj x: '))
    y = int(input('podaj y: '))
    if x <= y:
        print('jest ok')
        break
    else:
        print('x powinno byc mniejsze od y')

lista = [random.randint(x, y) for i in range(n)]
print(f'wygenerowana lista: {lista}')
quicksort(0, n - 1, lista)
print(f'posortowana lista: {lista}')
z = int(input('Jakiej liczby szukasz? '))
print(f'szukana liczba znajduje sie na indeksie: {binarysearch(lista,0,n,z)}')
