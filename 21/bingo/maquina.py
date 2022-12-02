from modulos import *


def verificarBolilla(mazo,bollilla,listado:list):
    for i in range(len(mazo)):
        for j in range(len(mazo[i])):
            for k in range(len(mazo[i][j])):
                if mazo[i][j][k] == bollilla:
                    listado[i][j][k] = 0

def verificarFilaMaquina(listado:list,listaParalela,numBaraja):
    for i in range(len(listado)):
        if listado[i][0]== 0 and listado[i][1]== 0 and listado[i][2]== 0 and listaParalela[i] == 0 :
            listaParalela[i] += 1
            print(f'La maquina hizo linea con el numero de carton {numBaraja+1} fila {i+1}')
def verificadorColumnaMaquina(listado:list,listaParalela,numBaraja):
    for i in range(len(listado[1])):
        suma = 0
        for j in range(len(listado)):
            suma += listado[j][i] 
        if suma == 0 and listaParalela[i] == 0:
            listaParalela[i] += 1
            print(f'La maquina hizo linea con el numero de carton {numBaraja+1} columna {i+1}')


def verificadorDeBingo(columna,fila,carton):
    if 0 not in columna and 0 not in fila:
        print(f'BINGO!!!!!\nLa maquina hizo bingo en el carton: {carton+1}')
        return 0
    return True