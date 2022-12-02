import random

def menu():
    return int(input('opcion 1: que siga el juego!!!\nopcion 2 ver los cartones\nopcion 3: linea\nopcion 4:Bingo!!!\nopcion 5: Tachar un casillero\nopcion: '))


def mazos(n,color='\033[32m',mostrar=False):
    baraja = []
    for i in range(n):
        baraja.append(generadorDeCarton(3,9))
        if mostrar == True:
            print(color+f'baraja {i+1}')
            printVect(baraja[i])
    return baraja
def verificarMazo(num,min,max,nombre):
    while num < min or num > max:
        num = int(input(f'porfavor elija un numero entre {min} y {max}, {nombre}: '))
    return num
def verificar(num,columna:list,max=99,min=1):
    while num < min or num > max or num in columna:
        num = random.randint(min,max)
    return num
def generadorDeCasilleros(carton:list):
    columna0 = []
    columna1 = []
    columna2 = []
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            if carton[i][j] == 0:
                numeroInsertar = random.randint(1,99)
                if j == 0:
                    carton[i][j] = verificar(numeroInsertar,columna0,max=11)
                    columna0.append(carton[i][j])
                elif j == 1:
                    carton[i][j] = verificar(numeroInsertar,columna1,max=22,min=12)
                    columna1.append(carton[i][j])
                else:
                    carton[i][j] = verificar(numeroInsertar,columna2,min=23)
                    columna2.append(carton[i][j])
def generadorDeCarton(filas,columna):
    carton = [[0]*filas for i in range(columna)]
    generadorDeCasilleros(carton)
    return carton
def printVect(vect:list):
    for i in vect:
        print(i)
def generedadorBolilla(n,lista):
    while n in lista:
        n = random.randint(1,99)
    return n