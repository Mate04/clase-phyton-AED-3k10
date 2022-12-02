import random
def menu():
    return int(input('\033[37m'+f'Opcion 1: tachar numero\nOpcion 2: Mostrar Barajas\nOpcion 3: Mostar baraja en particular\nOpcion 4: mostrar numero Tachados\nOpcion 5: Tachar Fila\nOpcion 0: Pasar a la siguiente ronda\n'))
def verificar(n,min,max):
    while min > n or n > max:
        n = int(input(f'elija una opcion valida entre {min} y {max}: '))
    return n
def generadorDeCarton():
    matriz = [[None]* 9 for i in range(3)]
    generadorDeNumeros(matriz)
    return matriz
def generadorDeNumeros(matriz:list):
    for i in range(len(matriz)):
        casillaVacia = random.randint(3,5)
        while matriz[i].count(None) > casillaVacia:
            generarNumero(i,matriz[i])
def generarNumero(fila,vect):
    posicion = random.randint(0,8)
    while vect[posicion] != None:
        posicion = random.randint(0,8)
    insertarNumero = generadorNumeberFila(fila)
    while insertarNumero in vect:
        insertarNumero = generadorNumeberFila(fila)
    vect[posicion] = insertarNumero
def generadorNumeberFila(fila):
    numeroPorFila = {
        0: random.randint(1,11),
        1: random.randint(12,22),
        2: random.randint(23,99)
    }
    return numeroPorFila[fila]

def printCarton(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
def generadorDeBarajas(n,barajas:list,bandera=False,color='white'):
    for i in range(n):
        barajas.append(generadorDeCarton())
    if bandera:
        printBarajas(barajas,color)
    return barajas
def printBarajas(matriz,color='white'):
    colores ={
        'red': '\033[31m',
        'white': '\033[37m',
        'blue': '\033[36m'
    }
    for i in range(len(matriz)):
        print(colores[color]+f'barajas {i+1}')
        for j in matriz[i]:
            print(j)
def printBaraja(vect,color='white'):
    colores ={
        'red': '\033[31m',
        'white': '\033[37m',
        'blue': '\033[36m'
    }
    print(colores[color])
    for i in range(len(vect)):
        print(vect[i])
def tacharNumero(barajaTachon, numBaraja,numCarton):
    barajaTachon[numBaraja].append(numCarton)
def verificarLinea(vect:list,listNum:list):
    for i in vect:
        if i not in listNum:
            return False
    return True
def matrizTransVersal(m:list):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez