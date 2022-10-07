from operator import le


def menu():
    return int(input('opcion 1: cargar\nBusqueda ID binaria\nopcion 3: punto 3\nopcion 0: SALIR\nopcion: '))
def busquedaBinaria(vect:list,x:int):
    dim = len(vect)
    cont = 0
    izq = 0
    der = dim
    bandera = True
    while izq <= der and cont < dim:
        mitad = (izq+der)//2
        if vect[mitad].ID == x:
            print('se encontro la busqueda\n',vect[mitad])           
            bandera = False
            break
        elif vect[mitad].ID > x:
            der = mitad
        elif vect[mitad].ID < x:
            izq = mitad
        cont += 1
    if bandera:
        print(f'no se encontro el resultado id: {x}')
def punto3(vect:list):
    matriz= [[0]*30 for i in range(20)]
    print(len(matriz))
    print(len(matriz[1]))