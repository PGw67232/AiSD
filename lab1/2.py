n=int(input("podaj dlugosc ciagu: "))
licznik=0
if n>0:
    for i in range(n):
        x=int(input(f"podaj {i} liczbe: "))
        if x<0:
            licznik+=1
    print(f"tyle liczb ujemnych podałeś: {licznik}")
else:
    print("proszę podac n wieksze od zera")

    
