from modulos import *

def main():
    op = 1
    ventas = []
    while op != 0:
        if op == 1:
            n = int(input('cuantos datos quiere cargar: '))
            cargar(ventas,n)
            Mostrar(ventas)
        if op == 2:
            x = int(input('que numero de filtro mayor de monto quiere agregar: '))
            t = input('distinto a que letra: ').upper()
            punto2(ventas,x,t)
        if op == 3:
            z = int(input('ingrese q tipo de perfume, para ver su total: '))
            conteo = vectConteo(ventas,z)
        if op == 4:
            punt4 = punto4(ventas)
            if punt4 == True:
                print('nunca cumplio el criterio')
        if op == 5:
            n = int(input('que tipo de factura desea buscar: '))
            p = int(input('que importe menor quiere buscar: '))
            punt5 = punto5(ventas,n,p)
            if punt5 == True:
                print('No se encontro resultado')
        #TODO: menu opciones
        op = int(input('ingrese una opcion\n(1) Cargar Vector\n(2) punto 2\n(3)Punto 3\n(4)Punto 4\nOpcion: '))
main()