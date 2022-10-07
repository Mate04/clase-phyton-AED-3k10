import os
import pickle

def menu():
    return int(input('Opcion 1: cargar\nopcion 2: punto 2\nopcion 3: punto 3\nopcion 0: Salir\nOpcion: '))
def punto2(vect,fd,x):
    writeBinary(fd,vect,x)
    readBinary(fd)
def writeBinary(fd,vect:list,x):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            if (3 <= i.numero <= 5) and i.importe > x:
                newList.append(i)
        pickle.dump(newList,m)
    m.close()
def readBinary(fd):
    with open(fd,'rb') as m:
        if not os.path.exists(fd):
            print('El archivo no existe')
        else:
            a = pickle.load(m)
            for i in a:
                print(i)
#punto 5
def busquedaBinaria(vect:list,x):
    dim = len(vect)
    izq = 0
    der = dim-1
    cont = 0
    while izq <= der and cont < dim:
        mitad = (der+izq)//2
        if vect[mitad].dni == x:
            return vect[mitad]
        elif vect[mitad].dni < x:
            der = mitad
        else:
            izq = mitad
        cont +=1
    return None
def punto3(vect,x):
    a = busquedaBinaria(vect,x)
    if a != None:
        print(f'el resultado es el sig\n{a}')
    else:
        print('no se encontro')
def punto4(vect,x):
    for i in vect:
        if i.nombre == x:
            print(i)
def punto5(vect,x):
    for i in vect:
        if i.afiliacion == x:
            print(i)
def punto6(vect):
    matriz = [[0]*15 for i in range(5)]
    for i in vect:
        matriz[i.afiliacion][i.numero-1] += 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                print(f'la fila {i} columna {j}: {matriz[i][j]}')
