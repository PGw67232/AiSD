tab = [1,2,3,11,21,111,231]
tab = sorted(tab)
tab_str = []
wynik = []
for x in tab:
    tab_str.append(str(x))
tab_str = sorted(tab_str)
for i in tab_str:
    wynik.append(int(i))
print(wynik)