from numpy import*
#il NL=nombre de ligne / NC=nombre de colone
def saisir_dimontion():
    global NL,NC
    NL=int(input('NL='))
    NC=int(input('NC='))
    while not(2<=NL<=20 and 1<=NC<=20):
        NL=int(input('NL='))
        NC=int(input('NC='))
    NC+=1
#kol ligne fih des colone mechi na3mlou il parcour mte3hom
def romplir_MAT(M,NL,NC):
    #il for loula bech na3mou il parcour mte3 les lignes
    for i in range(NL):
        #il for il theniya bech na3mlou il parcour mte3 les colones fi kol ligne
        for j in range(NC-1):
            M[i,j]=int(input('M['+str(i+1)+','+str(j+1)+']='))
            while not(0<=M[i,j]<=20):#condition
                M[i,j]=int(input('M['+str(i+1)+','+str(j+1)+']='))
#bech na3mlou il somme mte3 les colones fi kol linge
def somme(M,NL,NC):
    for i in range(NL):
        #kol mara ye7seb il somme mte3 il valeur mt3 les colone mte3 kol linge
        s=0
        for j in range(NC-1):
            s+=M[i,j]
        M[i,NC-1]=s
def affiche(M,NL,NC):
    #bech na3mel il affichage :1+2+3=6
    for i in range(NL):
        ch=''
        for j in range(NC-1):
            if j<NC-2:
                ch=ch+str(M[i,j])+"+"
            else:
                ch=ch+str(M[i,j])
        print(ch,'=',str(M[i,NC-1]))
            

#APP
saisir_dimontion()
M=array([[int()]* NC for i in range(NL)])
romplir_MAT(M,NL,NC)
somme(M,NL,NC)
affiche(M,NL,NC)