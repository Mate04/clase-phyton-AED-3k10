import os
from turtle import fd
from modulo import *
from registro import cargar

def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/contenidos.dat'
    op:int = 1
    contenidos = []
    bandera = False
    while op != 0:
        if op == 1:
            cargar(contenidos, int(input('cuanto contenido quiere cargar: ')))
            bandera = True
        if bandera:
            if op == 2:
                punto2(contenidos,int(input('cual es el filtro de mayor reproducciones que quiere poner: ')))
            elif op == 3:
                punto3(contenidos)
            elif op == 4:
                writeBinaria(fb,contenidos,int(input('mayor calificacion: ')))
                readbinaria(fb)
        else:
            print('porfavor primero cargue el vector')
        op = menu()
main()