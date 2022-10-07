import pickle
import os.path
from registro import *


# Funciones de validación
def validar_mayor_a(num, mensaje):
    n = int(input(mensaje))
    while n <= num:
        print('\nError...')
        n = int(input(mensaje))
    return n


def validar_mayor_a_float(num, mensaje):
    n = float(input(mensaje))
    while n <= num:
        print('\nError...')
        n = float(input(mensaje))
    return n


# Funciones afines al P4
def mostrar_menu():
    r = '\n------ Menu de opciones ------\n' \
        '1) Cargar vector.\n' \
        '2) Mostrar vector filtrado.\n' \
        '3) Matriz de conteo.\n' \
        '4) Crear archivo filtrado.\n' \
        '5) Mostrar archivo.\n' \
        '0) Salir.\n' \
        '------------------------------\n'
    return r


def add_in_order(reg, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if reg.id == v[c].id:
            pos = c
            break
        # ordenamos de menor a mayor
        if reg.id < v[c].id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def cargar_vector_empleos(n, v):
    for i in range(n):
        reg = generar_empleo_aleatorio()
        add_in_order(reg, v)
    if len(v) != 0:
        print('\nVector cargado correctamente...')


def mostrar_vector_empleos(v):
    for empleo in v:
        if 0 <= empleo.ciudad <= 10:
            print(to_string(empleo))
    if len(v) != 0:
        print('\nVector mostrado correctamente...')


def generar_matriz(v):
    m = [[0] * 20 for f in range(30)]
    for empleo in v:
        fila = empleo.ciudad
        col = empleo.tipo
        m[fila][col] += 1
    return m


def mostrar_matriz(mat, a, b):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if a <= mat[f][c] <= b:
                print('\nCantidad de empleos de la ciudad ' + str(f) +
                      ' y tipo de trabajo ' + str(c) + ': ', str(mat[f][c]))


def generar_archivo_filtrado(nombre_archivo, v, p):
    m = open(nombre_archivo, 'wb')
    for empleo in v:
        if empleo.monto > p and empleo.tipo <= 15:
            pickle.dump(empleo, m)
    m.close()

    if os.path.exists(nombre_archivo):
        print('\nArchivo creado exitosamente...')


def mostrar_archivo_filtrado(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('\nArchivo inexistente...')
        return
    c = 0
    tam = os.path.getsize(nombre_archivo)
    m = open(nombre_archivo, 'rb')
    while m.tell() < tam:
        reg = pickle.load(m)
        c += 1
        print(to_string(reg))
    m.close()
    print('\nSe mostraron ' + str(c) + ' registros...')
