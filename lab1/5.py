tab2d = [[1, 2, 3], [4, 5, 6], [-1, -2, -3], [-4, -5, -6]]
print(tab2d)
for w in tab2d:
    minw = min(w)
    mini = w.index(minw)
    w[0], w[mini] = w[mini], w[0]

print(tab2d)
