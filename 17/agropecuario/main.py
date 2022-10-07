from modulos import *

def MateoMaldonado():
    trabajos = []
    op = 1
    while op != 0:
        if op == 1:
            cargar(trabajos,Validar(int(input('cuantos trabajos quiere procesar '))))
            printVector(trabajos)
        if op == 2:
            punto2(trabajos)
        if op == 3:
            punto3(trabajos)
        if op == 4:
            Punto4(trabajos)
        if op == 5:
            num = int(input('que DNI deseas buscar: '))
            t = int(input('Que tipo deseas buscar: '))
            bandera = punto5(trabajos,num,t)
            if bandera:
                print('no se encontro resultados')
        op = int(input('(1) Cargar Datos\nPunto 2\nPunto 3\nPunto 4\nPunto 5\nIngrese Opcion: '))
MateoMaldonado()