import os
from modulos import *
from registro import *
def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/poliza.dat'
    op  = menu()
    poliza = []
    while op != 0:
        if op == 1:
            cargar(poliza,int(input('cuantos datos quiere cargar: ')))
        elif len(poliza) > 0:
            if op == 2:
                punto2(poliza,int(input('que formas de pago no quiere que se muestre: ')))
            elif op == 3:
                punto3(poliza)
            elif op == 4:
                punto4(poliza,fb,int(input('que precio quiere que sea mayor: ')))
        else:
            print('porfavor carge el vector')
        op = menu()
main()