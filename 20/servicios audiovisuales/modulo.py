

import os
import pickle


def menu():
    return int(input('opcion 1: cargar \nopcion 2:punto 2\nopcion 3: punto 3\nopcion 4: punto 4\nopcion 0: salir\nopcion: '))
#punto 2
def punto2(vect:list,c:int):
    for i in vect:
        if i.reproducciones > c:
            print(i)
#punto 3
def conteo(vect:list):
    #columna, fila
    matriz = [[0]*13 for i in range(15)]
    for i in vect:
        matriz[i.tipo-1][i.calificacion] += i.reproducciones
    return matriz
def printMatriz(vect:list):
    for i in range(len(vect)):
        for j in range(len(vect[i])):
            if vect[i][j] != 0:
                print(f'fila {i} columna {j}:',vect[i][j])
def punto3(vect:list):
    printMatriz(conteo(vect))
#punto 4
def writeBinaria(fd,vect:list,n):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            if (not(i.tipo == 4 or i.tipo == 8 or i.tipo == 12)and i.calificacion > n):
                newList.append(i)
        pickle.dump(newList,m)
    m.close()
def readbinaria(fd):
    contador = 0
    if not os.path.exists(fd):
        print('no existe el archivo que intenta leer')
    else:
        with open(fd,'rb') as m:
            a = pickle.load(m)
            for i in a:
                contador += i.reproducciones 
                print(i)
        if contador != 0:
            print('el total de reproducciones son','$'+contador)
        m.close()