import os
import pickle


def menu():
    return int(input('opcion 1: cargar\nopcion 2: filtro de zona geografica\nopcion 3: punto 3\nopcion 4: lectura y escritura binaria\nopcion 0: salir\nopcion 5: punto 6\n'))
def busquedaBinario(vect,num):
    dimension = len(vect)
    cont = 0
    inf = 0
    sup = dimension
    while inf <= sup and cont < dimension:
        mitad = (inf+sup)//2
        if vect[mitad].id == num:
            return mitad
        elif vect[mitad].id > num:
            sup = mitad
        elif vect[mitad].id < num:
            inf = mitad
        cont += 1
    return None
"""
Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea.  Muestre solo los registros cuyo lugar de origen sea diferente del valor p que se carga por teclado.
"""
def punto2(vect,p):
    for i in vect:
        if i.lugar != p:
            print(i)

def punto3(vect,num):
    pos = busquedaBinario(vect,num)
    if pos != None:
        print(f'se encontro resultado\n{vect[pos]}')
    else:
        print('no se encontro')
#punto 4 y 5
def writeBinary(fd,vect,tip):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            if i.tipo != tip:
                newList.append(i)
        pickle.dump(newList,m)
    m.close()
def readBinary(fd):
    if not os.path.exists(fd):
        print('no existe el archivo que desea leear')
    else:
        cantRegistro = 0
        sumaVenta = 0
        with open(fd,'rb') as m:
            lista = pickle.load(m)
            if len(lista) > 0:
                for i in lista:
                    cantRegistro += 1
                    sumaVenta += i.precio
                    print(i)
                print(f'el promedio de la venta fue de: {promedio(suma=sumaVenta,total=len(lista))}')
                print(f'y hubo una cantidad de registro: {cantRegistro}')
            else:
                print('no se encontro ningun elemento que cumpliera con la condicion la ultima vez que se cargo el archivo')
def promedio(suma,total):
    if total == 0:
        return None
    return suma/total
#punto 6
def punto6(vect):
    matriz = [[0]*30 for i in range(25)]
    for i in vect:
        if (4 <= i.lugar <= 15) and (2 <= i.tipo <= 10):
            matriz[i.lugar][i.tipo] += i.precio
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                print(f'fila {i} columna {j}: {matriz[i][j]}')