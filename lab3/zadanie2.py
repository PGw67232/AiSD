lista = [1,2,3,4,5]

def odwrocenie(liczby):
    if len(liczby) == 1:
        return liczby
    else:
        return odwrocenie(liczby[1:]) + liczby[0:1]  # Nie rozumiem do konca tego 
    
print(odwrocenie(lista))


