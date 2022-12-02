from modulo import *
from registro import cargar
import os
def main():
    fb = f'{os.path.dirname(os.path.realpath(__file__))}/articulos.dat'
    op = menu()
    articulos = []
    while op != 0:
        if op == 1:
            cargar(articulos, int(input('cuantos productos quiere cargar: ')))
        elif len(articulos) > 0:
            if op == 2:
                punto2(articulos,int(input('cual lugar geografico no quiere se muestre: ')))
            elif op == 3:
                punto3(articulos,int(input('que id deseas buscar: ')))
            elif op == 4:
                writeBinary(fb,articulos,int(input('que tipo de venta deseas obviar, para guardar el archivo: ')))
                readBinary(fb)
            elif op == 5:
                punto6(articulos)
        op = menu()
main()