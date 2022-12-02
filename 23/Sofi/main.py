from clase import *
import random
import pickle
import os
def validar_n():
    n = int(input("Ingrese la cantidad de eventos a cargar!"))
    while n <= 0:
        print("ERROR! Debe cargar una cantidad mayor a 0!")
    return n
def menu():
    print("Menu de opciones!")
    print("Op 1: Generar arreglo.")
    print("Op 2: Mostrar el arreglo")
    print("Op 3: Archivo con datos de montos mayores a p")
    print("Op 4: Mostrar archivo")
    print("Op 5: No programada")
    print("Op 6: Buscar id")
    print("Op 7: Matriz")
    print("Op 8: Determinar cuantas palabras comienzan con una mayuscula e incluyen una t y una s")
    print("Op 9: Salir!")

def generar_arreglo():
    cod = ("AB234", "CD765", "EF8QE", "SS222")
    tit = ("Inundacion", "Terremoto", "Incendio", "Sequia")
    desc = ("El Terremotos tuvo su epicentro en San Juan.", "Se Tractores inundo Cba.","Se Intentos incendio Ctes.", "Se Asecot Bs As.")
    id = random.choice(cod)
    titulo = random.choice(tit)
    descripcion = random.choice(desc)
    costo = round(random.uniform(500, 1500), 2)
    tipo = random.randint(0, 19)
    segmento = random.randint(0, 9)
    evento = Evento(id, titulo, descripcion, costo, tipo, segmento)
    return evento

def cargar_arreglo(vec, n):
    for i in range(n):
        evento = generar_arreglo()
        add_in_order(vec, evento)

def mostrar_vec(vec):
    for i in range(len(vec)):
        print(vec[i])

def add_in_order(vec,evento):
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c]. id == evento.id:
            pos = c
            break
        if vec[c].id > evento.id:
            der = c -1
        else:
            izq = c +1
    if izq > der:
        pos = izq

    vec[pos:pos] = [evento]

#3. A partir del arreglo, generar un archivo binario de registros que contenga los datos de todos los eventos cuyo monto
#de producción sea mayor a un valor p que se carga por teclado. Cada vez que esta opción se seleccione, el archivo debe
#crearse otra vez, eliminando los anteriores registros que hubiese contenido.

def punto_3(archivo, vec, p):
    m = open(archivo, "wb")
    for evento in vec:
        if evento.costo > p:
            pickle.dump(evento, m)
    m.close()
#4. Mostrar todos los datos del archivo que generó en el punto 3, a razón de un registro por línea.

def mostrar_archivo(archivo):
    if not os.path.exists(archivo):
        print("El archivo no fue creado!")
    else:
        m = open(archivo, "rb")
        tam = os.path.getsize(archivo)
        while m.tell() < tam:
            evento = pickle.load(m)
            print(evento)
        m.close()

#5. Recorra el archivo que generó en el punto 3, y genere a partir de él un arreglo unidimensional de valores de tipo
#float, que contenga en cada casilla solo el monto de producción de los eventos del archivo cuyo tipo de evento sea mayor
#o igual a 5. Muestre el arreglo generado de esta forma, y al final del listado agregue una línea adicional indicando el
#promedio de los montos mostrados.

#6. Determine si existe en el arreglo creado en el punto 1, un evento cuyo código de identificación coincida con el valor
#cod que se carga por teclado. Si existe, muestre sus datos completos, detenga la búsqueda y retorne la cadena contenida
#en el campo descripción del evento. Si no existe, informe con un mensaje y retorne la cadena “No existe.”.

def punto_6(vec, cod):
    n = len(vec)
    pos = None
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c]. id == cod:
            pos = c
            break
        if vec[c].id > cod:
            der = c -1
        else:
            izq = c +1
    return pos, vec[pos].descripcion
    #if pos is None:
    #    print("No existe.")
    #else:
    #    print(vec[pos].descripcion)

#7. A partir del arreglo creado en el punto 1, determine cuántos eventos existen para cada una de las posibles combinaciones
#entre tipos de evento y segmentos diarios (un total de 20 * 10 = 200 contadores). Genere todos los contadores posibles,
#pero muestre solo los resultados que correspondan a los tipos de evento mayores a 7.

def punto_7(vec):
    mat = [[0] * 10 for i in range(20)]
    for evento in vec:
        fila = evento.tipo
        columna = evento.segmento
        mat[fila][columna] += 1
    return mat

def mostrar_matriz(mat):
    cad = "Para el tipo de evento {} y segmento {} hay un total de {} eventos"
    for f in range(8, len(mat)):
        for c in range(len(mat[f])):
            print(cad.format(f, c, mat[f][c]))

#8. Tome la cadena retornada en el punto 6 (si existía el registro buscado), y determine cuántas palabras de esa cadena
#comenzaban con una letra mayúscula y tenían al menos una t y una s (en cualquier orden y no necesariamente seguidas).
#Como se dijo, la cadena debe terminar con un punto y las palabras deben separarse entre ellas con un (y solo un) espacio
#en blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella.

def procesar_texto(descripcion):
    cl = c_pal_mayus_st = 0
    empieza_mayus = tiene_st = False
    for letra in descripcion:
        if letra != " " or letra != ".":
            cl += 1
            if cl == 1 and "A" <= letra <= "Z":
                empieza_mayus = True
            if letra.lower() == "s" or letra.lower() == "t":
                tiene_st = True
        else:
            if empieza_mayus and tiene_st:
                c_pal_mayus_st += 1
            cl = 0
            empieza_mayus = False
            tiene_st = False
    return c_pal_mayus_st

def main():
    vec = []
    op = 0
    archivo = "Eventos.dat"
    descripcion = ""
    while op != 9:
        menu()
        op = int(input("Ingrese una opcion!"))
        if op == 1:
            n = validar_n()
            cargar_arreglo(vec, n)
        elif op == 2:
            if vec != []:
                mostrar_vec(vec)
            else:
                print("Debe cargar el arreglo!")
        elif op == 3:
            p = float(input("Ingrese un monto: "))
            punto_3(archivo, vec, p)
            print("Archivo creado!!")
        elif op == 4:
            mostrar_archivo(archivo)
        elif op == 5:
            print("Opcion no programada")
        elif op == 6:
            if vec != []:
                cod = input("Ingrese un id: ")
                pos, descripcion = punto_6(vec, cod)
                if pos != -1:
                    print(vec[pos].descripcion)
                else:
                    print("No existe.")
        elif op == 7:
            mat = punto_7(vec)
            mostrar_matriz(mat)
        elif op == 8:
            cont = procesar_texto(descripcion)
            print("La cantidad de palabras que comienzan con una mayuscula y que contienen s y t es:", cont)
        elif op == 9:
            print("Hasta luego!!")
        else:
            print("La opcion seleccionada no es valida!!")


main()