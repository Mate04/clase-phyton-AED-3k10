import os
from modulos import busquedaBinaria, menu, punto3
from registro import cargar

def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/empleados.dat'
    op = 1
    empleos = []
    while op != 0:
        if op == 1:
            cargar(empleos,int(input('cuantos emepleos quiere cargar: ')))
        elif op == 2:
            busquedaBinaria(empleos,int(input('que desea ID desea buscar: ')))
        elif op == 3:
            punto3(empleos)
        op = menu()
main()