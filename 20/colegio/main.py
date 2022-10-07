import os
from registro import *
from modulo import *
def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/contenidos.dat'
    op = 1
    miembros =[]
    bandera = False
    while op != 0:
        if op == 1:
            cargar(miembros,int(input('Cuantos miembro quiere cargar: ')))
            bandera = True
        if bandera:
            if op == 2:
                punto2(miembros,fb,int(input('introduce la cantidad mayor el importe: ')))
            elif op == 3:
                punto3(miembros,int(input('cual DNi deseas buscar ')))
            elif op == 4:
                punto4(miembros,input('que nombre quiere buscar: '))
            elif op == 5:
                punto5(miembros,int(input('que afilacion de sea buscar')))
            elif op == 6:
                punto6(miembros)
        else:
            print('Porfavor carge el vector')
        op = menu()
main()