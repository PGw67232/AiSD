
'''
def binarne(liczba):
    wynik = []
    while liczba > 1:
        wynik.append(liczba%2)
        liczba //= 2
    print(wynik)


binarne(10)



'''
'''
def binary(number): 
    if number > 1: 
        decimal_to_binary(number//2) 
    else: 
        print(number % 2, end = '') # Nie potrafilem usunac None na koncu kazdego wyniku..
    return

#TEN DZIALA
'''
def binary(liczba):
    if liczba == 0:
        return 0
    else:
        return liczba%2 + 10*binary(liczba//2)

print(binary(1))