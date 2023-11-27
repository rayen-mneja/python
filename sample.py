from numpy import*
def afich(t,n):
    for i in range(n):
        print(t[i])
def romplir (t,n):
    for i in range (n):
        t[i]=int(input('ti='))
def tri_selection(t,n):
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
            if t[j]<t[p]:
                p=j
        if p!=i:
            aux=t [p]
            t[p]=t[i]
            t[i]=aux
def tri_bulle(t,n):
    echange=True
    while echange==True and n!=1:
        echange=False
        for i in range (n-1) :
            if t[i]>t[i+1]:
                aux = t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                echange=True
        n=n-1
def cherch(t,n):
    aux=False
    for i in range(n):
        if t[i]=='10':
            aux=True
    
t=array([int]*50)
n=4
romplir (t,n)
tri_bulle(t,n)
afich(t,n)