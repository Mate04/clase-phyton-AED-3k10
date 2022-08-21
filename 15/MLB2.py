import random
from modulo.funciones import verificador,porcentaje

def main():
    posicion = verificador(int(input('ingrese la cantidad posicion del jugador: ')),-1,-1)
    cantidadDehit = verificador(int(input('ingrese la cantidad de hit hasta 20: ')),0,20)
    arrayJugadores = []
    arrayDeTotalDeHit = []
    porcentajesDeHit = []
    for i in range(posicion):
        arrayJugadores.append([])
        for j in range(cantidadDehit):
            arrayJugadores[i].append(random.randint(0,30))
    for i in range(len(arrayJugadores)):
        porcentajesDeHit.append([])
        c = 0
        for j in arrayJugadores[i]:
            porcentajesDeHit[i].append([j ,porcentaje(j,100)])
            c += j
        arrayDeTotalDeHit.append(c)
    options = True
    while options != 0:
        options = int(input('1 para ver la suma de hit de una posicion\n2 Porcentaje de bateos por posicion\n3 Ver Matriz\n0 para salir: '))
        if options == 1:
            posicion = verificador(int(input('ingrese la posicion del jugador para ver su suma de hit: ')),1,len(arrayJugadores))
            print(arrayDeTotalDeHit[posicion-1])
        if options == 2:
            print(porcentajesDeHit[verificador(int(input('ingrese la posicion para ver su porcentaje de bateos')),1,len(porcentajesDeHit))-1])
        if options == 3:
            for i in range(len(arrayJugadores)):
                print(arrayJugadores[i])
if __name__ == '__main__':
    main()