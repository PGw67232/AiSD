def func(n):
    if n == 1:
        return 4
    else:
        return 1/(1-func(n-1))
    
print(func(100))