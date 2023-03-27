#Zadanie 1
# a)
def nwd1(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

# b)
def nwd2(a,b):
    if a!=b:
        return nwd2(a-b,b)
    else:
        return nwd2(a,b-a)
    return a




def nwdRekII(a,b):
    if b!=0:
        return nwdRekII(b, a%b)
    return a