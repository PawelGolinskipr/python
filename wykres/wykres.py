import re
import random
import matplotlib.pyplot as plt
from collections import Counter
x=random.randint(1,10)
lista=[]
for n in range(1,10000,1):
    lista.append(random.randint(1,10))
print(Counter(lista))
x=Counter(lista)
strr=re.findall("\d+",str(x))
listas=[[],[]]


for x in strr:
    if int(x) > 10:
        listas[1].append(x)
    else:
         listas[0].append(x)

#plt.xlabel("od 1 do 10")
#plt.ylabel("ile się pojawiło")
#plt.plot(listas[0],listas[1])
plt.bar(list(map(int,listas[0])),list(map(int,listas[1])))
print(listas[0])
print(listas[1])
plt.show()
