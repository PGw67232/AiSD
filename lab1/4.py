tab = [-3, -4, -9, 0, 1, 3, 15, 90, 9, 17, -1]
naj = tab[0]
for x in tab:
    if x <= naj:
        naj = tab[x]

print(f"najmniejsza liczba w liście to : {naj}")
