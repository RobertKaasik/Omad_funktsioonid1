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
#Kirjutage ruudu üks külg ja programm arvutab korraga pindala, perimeetri ja dioganaali
    P=4*a
    S=a*a
    D=(a**2)/2
    D=D**0.5
    
    K=(P, S, D)
    
    return K

def season(sea):
#kirjuta number 1-12 ja programm arvutab välja, mis aastaaeg on
   if sea == 12 or 1 <= sea <= 2:
       print("Talv")
   elif 0<kuu<3:
       print("Talv")
   elif  3 <= sea <= 5:
       print("Kevad")
   elif 6 <= sea <= 8:
       print("Suvi")
   elif 9 <= sea <= 11:
       print("sügis")
   else:
       print("Vale süntaks")
   return sea

def xor_uncipher(string:str, key: str)->str:
#Kodeeritud text dekodeeritakse
    result = ''
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result

def nal(a, e, y):
#Kasutaja teeb aastateks euro sissemakse 10% aastas ja saab igal aastal, näiteks 1 = 1,10
    a = int(input())
    e = int(input())
    y = int(input())

    nal = a
    year = y
    def money():
            if year >0:
                nal = a*1.1+e
                year = year -1
                return money()
            else:
                return nal

def is_prime(b):
#Kirjutame arvu vahemikus 1-1000 ja programm kirjutab selle arvu tõeseks või mitte (True or False)
    k=2
    while k*k<=b:
        if b%k==0:
            return False
        k+=1
    return True

def date(d,m,y):
#kirjutamispäev näiteks 26
#kirjuta näiteks kuu 6
#kirjuta näiteks aasta 2020
#Selle tulemusena saame õige kuupäeva või mitte(True or False)
    if d<0 or m<0 or y<0:
        return False
    mon=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400==0 or ((y%4==0) and (y%100 != 0)):
        mon[1]=29
    if m>=1 and m<=12:
       if d>0 and d<=mon[m-1]:
           return True
    return False