import pickle


def menu():
    return int(input('opcion 1: cargar\nopcion 2: punto 2\nopcion 3: punto 3\n'))
def punto2(vect,f):
    for i in vect:
        if i.formaPago != f:
            print(i)
def punto3(vect:list):
    matriz = [[0]*5 for i in range(20)]
    for i in vect:
        matriz[i.tipoPoliza][i.formaPago-1] += 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                print(f'fila {i} columna {j}: {matriz[i][j]}')
def punto4(vect,fd,p):
    writeBinary(vect,fd,p)
    readBinary(fd)
def writeBinary(vect,fd,p):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            if i.precio > p:
                newList.append(i)
        if len(newList) > 0:
            pickle.dump(newList,m)
    m.close()
def promedio(suma,total):
    if total <= 0:
        return None
    return suma/total
def readBinary(fd):
    c = 0
    with open(fd,'rb') as m:
        a = pickle.load(m)
        for i in a:
            print(i)
            c += i.precio
    m.close()
    print('el promedio de precio fue:',promedio(c,len(a)))
