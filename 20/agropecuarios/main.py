import os

from modulo import *
from registro import cargar

def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/operaciones.dat'
    op = menu()
    operaciones = []
    while op != 0:
        if op == 1:
            cargar(operaciones,int(input('cuantas operaciones quiere realizar: ')))
        if len(operaciones) > 0:
            if op == 2:
                punto2(operaciones,int(input('filtro de zona geografica, se mostraran mayores o iguales al sig num: ')))
            elif op == 3:
                punto3(operaciones,int(input('v1: ')),int(input('v2: ')))
            elif op == 4:
                punto4(operaciones,fb)
        else:
            print('porfavor CARGE el vector')
        op = menu()
main()