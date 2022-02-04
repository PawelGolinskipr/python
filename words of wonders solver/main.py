file=open("slowa.txt","r")
lines=file.readlines()
file.close()
litery=[]
unilitery=[]
slowa=[]
inp=input("podaj litery (po spacji)")
litery=list(inp)
for x in litery:
    if x not in unilitery:
        unilitery.append(x)
print(litery)
print("czekaj")
for x in lines:
    y=list(x)[:-1]
    sp=0
    if len(litery)>=len(y) and len(y)>2 :
        for z in unilitery:
            if list(y).count(z)<=litery.count(z):
                sp+=list(y).count(z)
    if sp>=len(y):
            #print(y)
            if y not in slowa:
                slowa.append(y)
    else: 0

for x in slowa:
    for y in x:
        print(y, end="")
    print()
