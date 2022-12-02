import random
vect = [5,7,9,8,2,3,4,1,0]
vectOrd = []
der = len(vect) - 1
dim = len(vect)
izq = 0
for i in range(len(vect)):
    while izq <= der:
        mitad = (der + izq)//2
        if mitad == vect[i]:
            pos = mitad
            break
        elif mitad > vect[i]:
            der = mitad-1
        else:
            izq = mitad+1