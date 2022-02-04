import tkinter as tks
tk=tks.Tk()
#global
licz=""
p=0
hei=4
wei=7
fin=[]
#def
def pier(nun):
    global licz
    global p
    licz+=str(nun)
    #print( "".join(map(str,licz)))
    p=int(licz)
    ek.config(text=p)
    #print(p)
    #print(licz)
def neg():
    global licz
    global p
    p=p*-1
    licz=str(p)
    ek.config(text=p)
    #print(p)
def us():
    try:
        global licz
        licz=licz[:-1]
        p=int(licz)
        ek.config(text=p)
    except ValueError:
        p=0
        licz=str(0)
        ek.config(text=p)
def fal(j):
    global licz
    global p
    global fin
    
    if j=="+":
        fin=[]
        fin=j+" "+str(p)
    elif j=="-":
        fin=[]
        fin=j+" "+str(p)
    elif j=="*":
        fin=[]
        fin=j+" "+str(p)
    elif j=="/":
        fin=[]
        fin=j+" "+str(p)
    else:
        #print()
        0
    licz=""
    p=""
def row():
    global licz
    global p
    global fin
    
    try:
        a=fin.split(" ")
        
        if type(a[1]) is int or float:
            if len(a)==2:
                if a[0]=="+":
                    p=float(a[1]) + float(p)
                    ek.config(text=p)
                    licz=""
            
            
                elif a[0]=="-":
                    p=float(a[1])-float(p)
                    ek.config(text=p)
                    licz=""
            
            
                elif a[0]=="*":
                    p=float(p)*float(a[1])
                    ek.config(text=p)
                    licz=""
            
            
                elif a[0]=="/":
            
                    p=float(a[1])/float(p)
                    ek.config(text=p)
                    licz=""
            else:
                ek.config(text="co tak napierdalasz operatory")    
        fin=[]    
    except:
        licz=""
        p=0
        fin=0
        ek.config(p)
    

#show
ek=tks.Label(tk,text="Podaj liczby",width=30,height=5,font=("",15))
ek.grid(row=0,column=0,columnspan=4)

#button
j=tks.Button(tk,text=1,width=wei,height=hei, command= lambda: pier(1))
dwa=tks.Button(tk,text=2,width=wei,height=hei, command= lambda: pier(2))
t=tks.Button(tk,text=3,width=wei,height=hei, command= lambda: pier(3))
c=tks.Button(tk,text=4,width=wei,height=hei, command= lambda: pier(4))
p=tks.Button(tk,text=5,width=wei,height=hei, command= lambda: pier(5))
s=tks.Button(tk,text=6,width=wei,height=hei, command= lambda: pier(6))
si=tks.Button(tk,text=7,width=wei,height=hei, command= lambda: pier(7))
osi=tks.Button(tk,text=8,width=wei,height=hei, command= lambda: pier(8))
d=tks.Button(tk,text=9,width=wei,height=hei, command= lambda: pier(9))
z=tks.Button(tk,text=0,width=wei,height=hei, command= lambda: pier(0))

prze=tks.Button(tk,text=",",width=wei,height=hei)
neg=tks.Button(tk,text="+/-",width=wei,height=hei, command=neg)

dod=tks.Button(tk,text="+",width=wei,height=hei, command= lambda: fal("+") )
odj=tks.Button(tk,text="-",width=wei,height=hei,command= lambda: fal("-") )
mn=tks.Button(tk,text="*",width=wei,height=hei,command= lambda: fal("*") )
dzi=tks.Button(tk,text="/",width=wei,height=hei,command= lambda: fal("/") )

us=tks.Button(tk,text="usun",width=wei,height=hei,command=us)
row=tks.Button(tk,text="=",width=wei,height=hei,command=row)

#grid
j.grid(row=4 , column=0, sticky="NW")
dwa.grid(row=4 , column=1 ,sticky="NW")
t.grid(row=4 , column=2 ,sticky="NW")
c.grid(row=3 , column=0 ,sticky="NW")
p.grid(row=3 , column=1 ,sticky="NW")
s.grid(row=3 , column=2 ,sticky="NW")
si.grid(row=2 , column=0 ,sticky="NW")
osi.grid(row=2 , column=1 ,sticky="NW")
d.grid(row=2 , column=2 ,sticky="NW")
z.grid(row=5 , column=1 ,sticky="NW")

prze.grid(row=5 , column=2 ,sticky="NW")
neg.grid(row=5 , column=0 ,sticky="NW")

dod.grid(row=4 , column=3 ,sticky="NW")
odj.grid(row=3 , column=3 ,sticky="NW")
mn.grid(row=2 , column=3 ,sticky="NW")
dzi.grid(row=5 , column=3,sticky="NW")

us.grid(row=7 , column=0 ,sticky="NW")
row.grid(row=7 , column=1 ,sticky="NW")


tk.title("kalkulator")
tk.geometry("300x500")
tk.mainloop()
