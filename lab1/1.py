import math

delta = 0
a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))
if a != 0:
    delta = (b ** 2) - (4 * a * c)
    if delta > 0:
        x1 = (b * (-1) - math.sqrt(delta)) / 2 * a
        x2 = (b * (-1) + math.sqrt(delta)) / 2 * a
        print(f"pierwsze miejsce zerowe = {x1}")
        print(f"drugie miejsce zerowe = {x2}")
        print(f"funkcja w osi oY przechodzi w ptk.: {c}")
    else:
        if delta == 0:
            x0 - b * (-1) / 2 * a
            print(f"jedno miejsce zerowe = {x0}")
            print(f"funkcja w osi oY przechodzi w ptk.: {c}")
        else:
            print("Brak pierwiastków :( ")
else:
    print("nawet paraboli nie ma , a co dopiero miejsca zerowe")
