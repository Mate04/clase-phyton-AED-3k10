import pickle
import random
from registro import Registro

def menu():
    return int(input('opcion 1: cargar datos\nopcion 0: salir\nopcion: '))

def cargar(vect:list,n):
    dim = len(vect)
    for i in range(n):
        dni = i + dim + 1
        nombre = random.choice(['a','b','c'])+str(i+dim)
        importe = random.randint(5000,15000)
        afilacion = random.randint(0,4)
        id = random.randint(0,14)
        vect.append(Registro(dni,nombre,importe,afilacion,id))
    vect = inserccion(vect)
    mostrarVect(vect)
def mostrarVect(vect:list):
    for i in vect:
        print(i)
def inserccion(vect:list):
    pos = 0
    aux = 0
    for i in range(len(vect)):
        pos = i
        aux = vect[i]
        while pos < 0 and vect[pos-1].dni < aux.dni:
            vect[pos]= vect[pos-1]
            pos -= 1
        vect[pos] = aux
    return vect
def busquedaBinario(vect,doc):
    dimension = len(vect)
    cont = 0
    inf = 0
    sup = dimension
    while inf <= sup and cont < dimension:
        mitad = (inf+sup)//2
        if vect[mitad].dni == doc:
            return mitad
        elif vect[mitad].dni > doc:
            sup = mitad
        elif vect[mitad].dni < doc:
            inf = mitad
        cont += 1
    return None
def punto3(vect,doc):
    x = busquedaBinario(vect,doc)
    if x != None:
        newImport = int(input('que tipo de importe quiere ingresar: '))
        if newImport > vect[x].importe:
            vect[x].importe = newImport
            print('el nuevo importe es de:',vect[x].importe)
        else:
            print('el importe es menor al importe que cargaste\n', vect[x])
    else:
        print('no se encontro resultado!!')
def binarioPunto5(vect,fb,x):
    newList = []
    with open(fb,'wb') as m:
        for i in range(len(vect)):
            if (3 <= vect[i].id <= 5) and vect[i].importe > x:
                newList.append(vect[i])
        pickle.dump(newList,m)
    m.close()
def readBinaria(fb):
    with open(fb,'rb') as m:
        vect = pickle.load(m)
    m.close()
    for i in vect:
        print(i)