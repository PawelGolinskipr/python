#Autor Paweł Goliński

import math


mainloop=True
macierzA=[]
macierzB=[]
macierzC=[] #tu beda glownie wyniki

def ShowMacierz(ktora_macierz):
    if ktora_macierz=="a":
        print("tak wyklada macierz a: ")
        i=1
        for x in macierzA[1:]:
            
            if i%macierzA[0]!=0: 
                print(str(x)+" ",end="")
            else:
                print(str(x)+" ")
            i+=1
    elif ktora_macierz=="b":
        print("tak wyklada macierz b: ")
        i=1
        for x in macierzB[1:]:
            
            if i%macierzB[0]!=0: 
                print(str(x)+" ",end="")
            else:
                print(str(x)+" ")
            i+=1
    elif ktora_macierz=="c":
        print("tak wyklada macierz c (wynik): ")
        i=1
        for x in macierzC[1:]:
            
            if i%macierzC[0]!=0: 
                print(str(x)+" ",end="")
            else:
                print(str(x)+" ")
            i+=1
    else:
        print("zjebalo sie")



def DodajDoA():
    while True:
        try:
            kol=0
            kol=int(input("Podaj ilosc kolumn macierzy A\n"))
            if kol==0:
                print("ilosc kolumn musi byc !=0")
                continue
            wiersz=0
            wiersz=int(input("podaj: ilosc wierszy macierzy A\n"))
            if wiersz==0:
                print("ilosc wierszy musi byc !=0")
                continue
            break
        except:
            print("Najpewniej dodano litery a nie liczby")
    
    macierzA.append(kol)
    while True:
            for x in range(kol*wiersz):
                try:    
                    podanaliczba=input("podaj "+str(x+1)+" liczbe\n")
                    macierzA.append(int(podanaliczba))
                except:
                    print("podaj liczby!")
                    macierzA.clear()
                    macierzA.append(kol)
                    break
            if len(macierzA)-1 == kol*wiersz:
                break


def DodajDoB():
    while True:
        try:
            kol=0
            kol=int(input("Podaj ilosc kolumn macierzy B\n"))
            if kol==0:
                print("ilosc kolumn musi byc !=0")
                continue
            wiersz=0
            wiersz=int(input("podaj: ilosc wierszy macierzy B\n"))
            if wiersz==0:
                print("ilosc wierszy musi byc !=0")
                continue
            break
        except:
            print("Najpewniej dodano litery a nie liczby")
    
    macierzB.append(kol)
    while True:
            for x in range(kol*wiersz):
                try:    
                    podanaliczba=input("podaj "+str(x+1)+" liczbe\n")
                    macierzB.append(int(podanaliczba))
                except:
                    print("podaj liczby!")
                    macierzB.clear()
                    macierzB.append(kol)
                    break
            if len(macierzB)-1 == kol*wiersz:
                break

def Dodawanie():
    if macierzA[0]==macierzB[0] and len(macierzB)==len(macierzA):
        macierzC.append(macierzA[0])
        for x in range(1,len(macierzA)):
            macierzC.append(macierzA[x]+macierzB[x] )
        return 1
    else:
        return 0
def Odejmowanie():
    if macierzA[0]==macierzB[0] and len(macierzB)==len(macierzA):
        macierzC.append(macierzA[0])
        for x in range(1,len(macierzA)):
            macierzC.append(macierzA[x]-macierzB[x] )
        return 1
    else:
        return 0
def Transpozycja(ktoramacierz):
    if ktoramacierz=="a":
        Copy=[]
        Copy.append(int((len(macierzA)-1)/macierzA[0]))       
        PierwszaLinia=0
        i=0
        for x in (range(1,len(macierzA))):
            #1 4 7 10 13 16 19
            #2 5 8 11 14 17 20
            #3 6 9 12 15 18 21
            if (len(Copy)-1)% Copy[0]==0:
                Copy.append(i+1)
                i+=1
                PierwszaLinia=0
            else:
                PierwszaLinia+=macierzA[0]
                Copy.append(i+PierwszaLinia)
    return Copy      

def Mnozenie():
    if macierzA[0]==((len(macierzB)-1)/macierzB[0]):
        macierzC.append(macierzB[0])
       
        for x in (range(0, int((len(macierzA)-1)/macierzA[0])* macierzB[0]  ) ):
           
            suma=0
            pomocB=0
                
            for y in range(macierzA[0]):
                    suma+=macierzA[(y+math.floor(x/macierzC[0])*macierzA[0]) +1]*macierzB[(pomocB+x%macierzC[0])+1]
                    #print(pomocA+math.floor(x/macierzC[0])+1)
                    #print(math.floor(x/macierzC[0]))
                    pomocB+=macierzB[0]
                    
            macierzC.append(suma)
                            
            

               
               
            

            
        
            
            
        return 1
    else:
        return 0
while mainloop:
    print("Opcje:")
    print("----------------------------------")
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. Transpozycja")
    print("4. mnozenie")
    print("5. exit")
    wybor=input()
    
    if(wybor=="1"):
        CzySieUdalo=0
        DodajDoA()
        DodajDoB()
        CzySieUdalo= Dodawanie()
        if CzySieUdalo==1:
            ShowMacierz("a")
            ShowMacierz("b")
            ShowMacierz("c")
        else:
            print("nie dales poprawnych danych!")
            print("przy dodawaniu kolumna macierzy A = kolumnie mecierzy B i to samo przy wierszach")

        macierzA.clear()
        macierzB.clear()
        macierzC.clear()
    elif wybor=="2":
        CzySieUdalo=0
        DodajDoA()
        DodajDoB()
        CzySieUdalo= Odejmowanie()
        if CzySieUdalo==1:
            ShowMacierz("a")
            ShowMacierz("b")
            ShowMacierz("c")
        else:
            print("nie dales poprawnych danych!")
            print("przy dodawaniu kolumna macierzy A = kolumnie mecierzy B i to samo przy wierszach")

        macierzA.clear()
        macierzB.clear()
        macierzC.clear()
    elif wybor=="3":
        DodajDoA()
        print("przed:")
        ShowMacierz("a")
        print("po:")
        macierzA=Transpozycja("a")
        ShowMacierz("a")
        macierzA.clear()
    elif wybor=="4":
        CzySieUdalo=0
        DodajDoA()
        DodajDoB()
        CzySieUdalo= Mnozenie()
        if CzySieUdalo==1:
            ShowMacierz("c")
        else:
            print("dales nie poprawne dane")
            print("kolumny macierzy A musza byc rowne wierszy macierzy B")
        macierzA.clear()
        macierzB.clear()
        macierzC.clear()
    elif wybor=="5":
        mainloop==False
    else:
        print("zly wybor")