import pickle
from turtle import fd

def menu():
    return int(input('opcion 1: cargar\nopcion 2: punto 2\nopcion 3: punto 3\nopcion 4: punto 4\nopcion: '))
def punto2(vect:list,z:int):
    for i in vect:
        if i.campo >= z:
            print(i)
def punto3(vect:list,v1,v2):
    matriz = [[0]*20 for i in range(15)]
    for i in vect:
        matriz[i.operacion-1][i.campo] += i.importe
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if v1 <= matriz[i][j] <= v2:
                print(f'fila {i} columna {j} = {matriz[i][j]}')
#punto 4
def promedio(sum,total):
    if total != 0:
        return sum/total
    else:
        return None 
def punto4(vect:list,fd):
    suma = 0
    for i in vect:
        suma += i.importe
    writeBynari(fd,vect,promedio(suma,len(vect)))
    readBinary(fd)
def writeBynari(fd,vect:list,prom):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            if i.importe > prom:
                newList.append(i)
        if len(newList) > 0:
            pickle.dump(newList,m)
        m.close()
def readBinary(fd):
    with open(fd,'rb') as m:
        cont = 0
        n = pickle.load(m)
        for i in n:
            cont += 1
            print(i)
        print(f'hubo {cont} registros')
    m.close()
def validar(num,max,min):
    while num < min  or max > num:
        num = int(input(f'porfavor elija un numero entre {min} y {max}'))
        return num
print(validar(-4,9,4))