
import random 

cantPant = 0
cantDivAnterio = 0
contPuntoC = 0
options = True
optionsPrimero2 = False
optionsPrimero = False
vueltaDada = False
vuelta = 0
array = []
EsteSiXD = 0

while options != 0:
    options = int(input('Ingresar una carga de numero finaliza en 0'))
    if options % 6 == 0:
        cantPant += 1
    if vueltaDada:
        if options != 0 and numAnterior % options == 0 :
            cantDivAnterio += 1
    if options % 2 != 0:
        if optionsPrimero:
            if anteanteAnterior < options:
                if optionsPrimero2:
                    if anteanteAnterior < options:
                        contPuntoC += 1
                    else:
                        optionsPrimero2 = False
                        optionsPrimero = False
                else:
                    optionsPrimero2 = True
                    anteanteAnterior = options
            else:
                optionsPrimero = False
        else:
            optionsPrimero = True
            anteanteAnterior = options
    else:
        optionsPrimero2 = False
        optionsPrimero = False
    if contPuntoC == 1 and optionsPrimero2 == False:
        EsteSiXD += 1

    numAnterior = options
    vueltaDada = True
print(EsteSiXD)
print(array)