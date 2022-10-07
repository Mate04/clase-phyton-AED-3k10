import os
from modulos import *
def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/ventas.dat'
    op = -1
    ventas = []
    while op != 0:
        if op == 1 or op == -1:
            if not os.path.exists(fb) or op == 1:
                cargar(ventas,int(input('cuannto archivos quiere cargar: ')))
                inserccion(ventas)
                creacionArchivoBinario(fb,ventas)
                print('se cargo exitosamente el arreglo!!!')
            else:
                ventas = lecturaArchivoBinario(fb,ventas)
        elif op == 2:
            printVectPunto2(ventas,int(input('que lugar quiere que no se muestre: ')))
        elif op == 3:
            punto3(vect=ventas)
        elif op == 4:
            punto4(ventas)
        elif op == 6:
            if os.path.exists(fb):
                ventas = lecturaArchivoBinario(fb,ventas)
        elif op == 8:
            if os.path.exists(fb):
                lecturaArchivoBinario2(fb)
        op = menu()
main()