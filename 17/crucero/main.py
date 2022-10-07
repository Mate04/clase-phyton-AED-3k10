from modulos import cargar, punto2, punto3,punto4,punto5

def main():
    op = 1
    ventas = []
    while op != 0:
        if op == 1:
            cargar(ventas,int(input('cuantas ventas quiere procesar: ')))
        elif op == 2:
            punto2(ventas)
        elif op == 3:
            punto3(ventas)
        elif op == 4:
            punto4(ventas)
        elif op == 5:
            pos = punto5(ventas,input('que pasaporte quiere buscar: '))
            if pos != None:
                print(f'pasero: {ventas[pos].name}')
            else:
                print('no se encontro pasajero ')
        op = int(input('seleccione una opcion\n(1)\n(2)\n(3)\n(4)\n(5)\nopcion: '))
main()