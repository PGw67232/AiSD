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

def bin_search(lista, left, right, szukana):
    left = 0
    right = n-1
    while left <= right:
        srodek = (left + right) // 2
        if lista[srodek] == szukana: return srodek
        elif lista[srodek] > szukana: right = srodek-1
        else: right = srodek+1

    return -1


def usun_duplikaty(lista):
    return list(set(lista))


while True:
    n = int(input("Podaj ilość elementów listy: "))
    if n <= 0: print("Podaj n>0")
    else: break

while True:
    x = int(input("Podaj przedział: od "))
    y = int(input(" do "))
    if x <= y: break
    else: print("Podaj poprawne dane")

lista = [random.randint(x,y) for i in range(n)]
print("Wygenerowana lista: ", lista)
quicksort(0,n-1,lista)
print("Posortowana lista: ", lista)
#trzeba dać duży przedział, żeby pozbyć się duplikatów
bez_dupl = usun_duplikaty(lista)
print("bez dupkl: ",bez_dupl)
'''z = int(input("Jakiej liczby szukasz? "))
print(f"szukana liczba znajduje sie na indeksie: {bin_search(lista, 0, n, z)}")'''
