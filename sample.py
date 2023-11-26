from numpy import*
def afich(t,n):
    for i in range(n+1):
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
t=array([int]*50)
n=4
romplir (t,n)
tri_selection(t,n)
afich(t,n)