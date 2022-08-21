class Jugador:
        def __init__(self, name, posicion):
            self.name = name
            self.posicion = posicion
        def getDataString(self):
            return f'{self.name} esta en la posicion {self.posicion} y tiene {self.cantidadDehit} hit'
        def getData(self):
            return [self.name,self.posicion,self.cantidadDehit]
def main():
    jugadores = generadorJugador(int(input('ingrese la cantidad de jugadores: ')))
    for i in jugadores:
        pass
def generadorJugador(n):
    arrayJugadores = []
    for i in range(n):
        name = input(F'nombre del jugador {i}: ')
        posicion =verificarPosicion(int(input(f'posicion del jugador {i}: ')))
        arrayJugadores.append(Jugador(name,posicion).getData())
    return arrayJugadores

def verificarCantidadDehit(num):
    while num < 0:
        num = int(input('ingrese una cantidad de hit valida: '))
    return num

def verificarPosicion(num):
    while num < 0 or num > 9:
        num = int(input('ingrese una posicion valida: '))
    return num

if __name__ == '__main__':
    main()