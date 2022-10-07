from modulos import *

def MateoMaldonado():
    niños = []
    op = 1
    while op != 0:
        if op == 1:
            cargar(niños,validarVector(int(input('Cuanto registro de estudiantes quiere procesar: '))))
            niños = min_to_max(niños)
            printVector(niños)
        if op == 2:
            contador(niños)
        if op == 3:
            dniAbuscar = int(input('DNI Tutor: '))
            importe = punto4(niños, dniAbuscar)
            if importe == 0:
                print('no se encontro el DNI buscado')
            else:
                print(f'El dni tutor {dniAbuscar} su importe es de {importe}')
        if op == 4:
            buscarApellido = input('Buscar apellido: ')
            punto5(niños,buscarApellido)
        op = int(input('opciones \n(1)Cargar mas Alumnos\n(2)Contador\n(3)Bsuqueda\n(4)"10%" de descuento\nOpcion: '))
MateoMaldonado()