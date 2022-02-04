import string
literyD=string.ascii_uppercase
literyM=string.ascii_lowercase
liczba=0
system=0
PoPrzeliczeniu_na_liczby=[]#żeby mozna bylo obliczbyc dla systemow +10
mainloop=True
while mainloop:
    PoPrzeliczeniu_na_liczby.clear()
    i=0
    print("podaj liczbe (dla systemow +10 wielkie litery albo 0 zeby zakonczyc program)")
    liczba= input()
    if liczba=="0":
        break
    print("podaj system")
    system=input()
    if int(system)>10+len(literyD):
        print("za duzy system max 36")
        continue
    
    for x in liczba:
        if x in literyD:
            PoPrzeliczeniu_na_liczby.append(int(literyD.index(x))+10)
        else:
            PoPrzeliczeniu_na_liczby.append(x)
    for x in PoPrzeliczeniu_na_liczby:
        try:    
            if int(x)>int(system)-1:
                i=1
        except:
            print("WIELKIE LITERY")
            i=1
            break
    if i==1:

        print("dales nie prawidlowe dane")
        continue
    print("L0="+str(PoPrzeliczeniu_na_liczby[0]))
    n=1
    wynik=int(PoPrzeliczeniu_na_liczby[0])
    for x in PoPrzeliczeniu_na_liczby[1:]:
        print("L"+str(n)+"="+str(wynik)+"*"+str(system)+"+"+str(PoPrzeliczeniu_na_liczby[n])+"=",end="")
        wynik=wynik*int(system)+int(PoPrzeliczeniu_na_liczby[n])
        print(str(wynik))
        n+=1
    
    print(wynik)
    
