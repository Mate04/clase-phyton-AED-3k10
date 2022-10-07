from modulos import *

def MateoMaldonado():
    op = 1
    ventas = []
    while op != 0:
        if op == 1:
            cargar(ventas,validarNumerodeCarga(int(input('Cuantas ventas quiere procesar: '))))
            printVect(ventas)
        if op == 2:
            x = int(input('x= '))
            y = int(input('y= '))
            punto2(ventas,x,y)
        if op == 3:
            punto3(ventas)
        if op == 4:
            punto4(ventas)
        if op == 5:
            t = int(input('que ticket desea buscar: '))
            if punto5(ventas,t):
                print('no se encontro el ticket')
        #menu options
        op = int(input('(1)cargar\n(2)Filtracion de numero de importes\n(3)Vector Conteo\n(4)el numero menor de importes\n(5)buscar Ticket\nEliga una opcion o 0 para salir: '))
MateoMaldonado()