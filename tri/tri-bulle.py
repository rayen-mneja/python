from numpy import*
t1=array([str]*20)
t2=array([str]*20)
def saisir_n():
    global n
    n=int(input('n='))
    while not(4<=n<=20):
        n=int(input('n='))
def remplir_t(t,n):
    for i in range(n):
        t[i]=input('t['+str(i)+']')
        while not(verif(t[i])==True and len(t[i])<=10):
            t[i]=input('t['+str(i)+']')
def verif(ch):
    aux=True
    i=0
    while not(aux==False or i==len(ch)):
        if ord('A')<=ord(ch[i])<=ord('Z'):
            i+=1
        else:
            aux=False
    return aux
def tri(t1,t2,n):
    for i in range(n):
        min=posmin(t1,n)
        t2[i]=t1[min]
        t1[min]='ZZZZZZZZ'
def posmin(t1,n):
    min=0
    for j in range(n-1):
        if point(t1[j])>point(t1[j+1]):
            min=j
    return min
def point(ch):
    s=0
    for i in range(len(ch)):
        s=s+ord(ch[i])
    return s
def affiche(t1,t2,n):
    print('t2=',t1[0],'t1=',t2[0])
    for i in range(1,n):
        print('t2=',t1[i])
saisir_n()
remplir_t(t1,n)
tri(t1,t2,n)
affiche(t1,t2,n)
            