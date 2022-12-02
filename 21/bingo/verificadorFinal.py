
import random
import time
from modulos import *

def verificarCartones(numerosSalidos:list,listaDeTachadasJugador:list):
    for i in range(len(listaDeTachadasJugador)):
        if len(listaDeTachadasJugador[i]) > 0:
            for j in range(len(listaDeTachadasJugador[i])):
                if listaDeTachadasJugador[i][j] not in numerosSalidos:
                    return False
    return True
def filasTachadas(tipo,posicion,carton,numerosSalidos):
    #columna
    if tipo == 1:
        for i in range(len(carton)):
            if carton[i][posicion] not in numerosSalidos:
                return False
        return True
    else:
        for i in range(len(carton[posicion])):
            if carton[posicion][i] not in numerosSalidos:
                return False
        return True
def ronda4():
    moneda = random.choice(['seca','cara'])
    print('toco...')
    time.sleep(0.1)
    print(moneda)
    if moneda == 'seca':
        return int(input('que numeor deseas q salga? '))
    else:
        return generadorDeCarton(3,9)
