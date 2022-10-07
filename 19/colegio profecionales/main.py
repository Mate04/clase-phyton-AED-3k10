from modulos import *
import os

def main():
    empleados = []
    op = 1
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/empleados.dat'
    while op != 0:
        if op == 1:
            cargar(empleados,int(input('cuantos empleos quiere cargar: ')))
        elif op == 2:
            punto3(empleados,int(input('cual id desea buscar: ')))
        elif op == 3:
            binarioPunto5(empleados,fb,int(input('que importe quiere que sea mayor: ')))
            readBinaria(fb)
        elif op == 4:
            pass
        op = menu()
main()