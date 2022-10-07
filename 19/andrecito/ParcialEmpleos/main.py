from funciones import *


def main():
    # Creamos variables principales
    FD = 'empleos.dat'
    v = list()
    op = -1

    while op != 0:
        print(mostrar_menu())
        op = validar_mayor_a(-1, '\nIngrese su opción: ')
        if op == 1:
            n = validar_mayor_a(0, '\nIngrese cantidad de empleos: ')
            cargar_vector_empleos(n, v)
        elif 2 <= op <= 5:
            if len(v) != 0:
                if op == 2:
                    mostrar_vector_empleos(v)
                elif op == 3:
                    mat = generar_matriz(v)
                    a = validar_mayor_a(-1, '\nIngrese el valor de la cota "a": ')
                    b = validar_mayor_a(0, '\nIngrese el valor de la cota "b": ')
                    mostrar_matriz(mat, a, b)
                elif op == 4:
                    p = validar_mayor_a_float(0, '\nIngres el monto a discriminar: ')
                    generar_archivo_filtrado(FD, v, p)
                elif op == 5:
                    mostrar_archivo_filtrado(FD)
            else:
                print('\nCargue el vector...')
        elif op == 0:
            print('\nSaludos...')
        else:
            print('\nOpción incorrecta...')


if __name__ == '__main__':
    main()
