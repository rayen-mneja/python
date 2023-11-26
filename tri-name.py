from numpy import *
t1=array([str]*40)
t2=array([int]*40)
def saisir_n():
    global n
    n=int(input('le nombre des eleves='))
    while not(n in range (1,40)):
        n=int(input('le nombre des eleves='))
def romplir_nom(t,n):
        for i in range(1,n+1):
            t[i]=input('t['+str(i)+']')
            while estalf(t[i])==False:
                t[i]=input('t['+str(i)+']')
def estalf(ch):
     aux=True
     i=0
     while not(aux==True):
        if ord('a')<= ord(ch[i]) <=ord('z'):
            i+=1
        else:
             aux=False
     return aux
def romplir_note(t,n):
     for i in range(1,n+1):
        t[i]=int(input('t2['+str(i)+']'))
        while not(0<=t[i]<=20):
            t[i]=int(input('t2['+str(i)+']'))
def tri_nom(t,n):
     echenge=True
     i=1
     ch1=t[i]
     while not(echenge==False or i==n-1):
         echenge=False
         for j in range(i+1,n):
             ch2=t[j]
             if ord(ch1[0])<ord(ch2[0]):
                 aux=t[i]
                 t[i]=t[j]
                 t[j]=aux
                 echenge=True
             elif ord(ch1[0])==ord(ch2[0]):
                 k=1
                 vix=False  
                 espas(ch1,)
                 while not(vix==True or k==len(ch2)):
                     

def espas()

