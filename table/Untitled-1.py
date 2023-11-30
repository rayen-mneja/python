from numpy import*
#il NL=nombre de ligne / NC=nombre de colone
def saisir_dimontion():
    global NL,NC
    NL=int(input('NL='))
    NC=int(input('NC='))
    while not(2<=NL<=20 and 1<=NC<=20):
        NL=int(input('NL='))
        NC=int(input('NC='))
#kol ligne fih des colone mechi na3mlou il parcour mte3hom
def romplir_MAT(M,NL,NC):
    #il for loula bech na3mou il parcour mte3 les lignes
    for i in range(NL):
        #il for il theniya bech na3mlou il parcour mte3 les colones
        for j in range(NC):
            M[i,j]=int(input('M['+str(i+1)+','+str(j+1)+']='))
            while not(0<=M[i,j]<=20):
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
M=array([[int()]* NC for i in range(NL)])
t=array([int]*NL)
romplir_MAT(M,NL,NC)
somme(M,NL,NC,t)
affiche(M,NL,NC,t)