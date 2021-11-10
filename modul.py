def arithmetic(a:float,b:float,c:str):
    #Lihtne kalkulaator
    #   + - liitmine 
    #   - - lahutamine
    #   * - korrutamine
    #   / - jagamine
    #   :param float a: Esimene arv
    #   :param float b: Teine arv
    #   :param str c: Aritmeetiline tehing
    #   :rtype float:

    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
    else:
        print("Viga")
        r=0.0
    return r

def is_year_leap(aasta: int):
    #Liigaasta leidmine
    #Tagastab true kui aasta on liigaasta ja False kui ei ole
    #:param int aasta: Aasta number
    #:rtype bool: Funktsioni vastus loogilises formaadis

    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus 

def square(a):
    P=4*a
    S=a*a
    D=(a**2)/2
    D=D**0.5
    
    K=(P, S, D)
    
    return K

def season(sea):
   if sea == 12 or 1 <= sea <= 2:
       print("Talv")
   elif  3 <= sea <= 5:
       print("Kevad")
   elif 6 <= sea <= 8:
       print("Suvi")
   elif 9 <= sea <= 11:
       print("sügis")
   else:
       print("Vale süntaks")
        n = int(input("Sisestage kuu number (1-12): "))

        season(n)