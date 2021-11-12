from modul import *
while True:
    print("Funktsioonid".center(50,"+"))
    print("arithmetic- A, \nis_year_leap-Y, \nsquare-N, \nseason-S, \nKooderimine-X, \nnalik-M, \nis_prime-P, \ndate-D")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1: "))
        arv2=float(input("Arv 2: "))
        sym=input("Tehe: ")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print(rezult)
    elif v.upper()=="N":
        rezult=square(int(input("Sisestage piirkond: ")))
        print(rezult)
    elif v.upper()=="S":
        rezult=season(int(input("Sisestage hooaeg: ")))
        print(rezult)
    elif v.upper()=="X":
        print("Kooderimine".center(60,"*"))
        rezult=xor_uncipher(input("sisesta text: "), input("Sisesta võti: "))
        print(rezult)
        print("Dekodeerimine".center(60,"*"))
        de_rezult=xor_uncipher(rezult, input("Sisesta võti: "))
        print(de_rezult)
    elif v.upper()=="M":
        a=float(input("Sisestage sissemakse summa: "))
        years=int(input("Mitu aastat on möödunud?"))
        rezult=nal(a,years)
        print(rezult)
    elif v.upper()=="P":
        rezult=is_prime(int(input("kirjutage arv vahemikus (1-1000): ")))
        print(rezult)
    elif v.upper()=="D":
        day=int(input("Sisestage päev: "))
        month=int(input("Sisestage kuu: "))
        year=int(input("Sisestage aasta: "))
        result=date(day,month,year)
        print(result) 