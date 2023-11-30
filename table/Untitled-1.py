from numpy import*
def saisir_dimontion():
    global NL,NC
    NL=int(input('NL='))
    NC=int(input('NC='))
    while not(4<=NL<=20 and 10<=NC<=20):
        NL=int(input('NL='))
        NC=int(input('NC='))
def romplir_MAT(M,NL,NC):
    for i in range(NL):
        for j in range(NC):
            M[i,j]=int(input('M['+str(i+1)+','+str(j+1)+']='))
            while M[i,j]>20 or M[i,j]<0:
                M[i,j]=int(input('M['+str(i+1)+','+str(j+1)+']='))
def somme(M,NL,NC,t):
    for i in range(NL):
        s=0
        for j in range(NC):
            s+=M[i,j]
        t[i]=s
def affiche(M,NL,NC,t):
    for i in range(NL):
        ch=''
        for j in range(NC):
            if j<NC-1:
                ch=ch+str(M[i,j])+"+"
            else:
                ch=ch+str(M[i,j])
        print(ch,'=',str(t[i]))
            

#APP
saisir_dimontion()
M=array([[int()]*NL for i in range(NC)])
t=array([int]*NL)
romplir_MAT(M,NL,NC)
somme(M,NL,NC,t)
affiche(M,NL,NC,t)