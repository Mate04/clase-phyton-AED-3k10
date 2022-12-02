
import os
from clase import *
import pickle

def menu():
    return int(input('        --------------MENU---------------\n'
                    '=================================================\n'
                    'Opcion 1: Mostrar los generos mediante un vector\n'
                    'Opcion 2: Procesar csv a matriz\n'
                    'Opcion 3: Filtro de duracion\n'
                    'Opcion 4:Vector Conteo\n'
                    'Opcion 5: Visualizar archivo Binario\n'
                    'Opcion 6: Busqueda Titulo\n'
                    'Opcion 0: Salir\n'
                    '=================================================\n'
                    'Ingrese una opcion : '))
def printVect(vect:list):
    for i in vect:
        print(i)
# funciones de validación
def validar_mayor_a(num, mensaje):
    n = int(input(mensaje))
    while n <= num:
        print('Error, ingrese un número mayor que ' + str(num) + '...')
        n = int(input(mensaje))
    return n


def validar_entre(inf, sup, mensaje):
    n = int(input(mensaje))
    while n < inf or n > sup:
        print('\nError, ingrese un valor comprendido entre ' + str(inf) + ' y ' + str(sup) + '....')
        n = int(input(mensaje))
    return n

# funciones del punto 1
def leer_generos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('\nArchivo inexistente...')
        return
    v = []
    m = open(nombre_archivo, 'rt')
    for linea in m:
        linea = linea[0:-1]
        v.append(linea)
    m.close()
    return v


def add_in_order(reg, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        mitad = (der+izq)//2
        if reg.votes == v[mitad].votes:
            pos = mitad
            break
        if reg.votes > v[mitad].votes:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def genre_to_int(genre, v_generos):
    for i in range(len(v_generos)):
        if genre == v_generos[i]:
            return i

def duracion_to_int(duracion):
    #remplazamos la duracion de un string vacio a un 0 para que sea escalble, y si deciden registrarlo puedan sacar a futuro estadisticas, y no haya un error o contemplar todo la informacion. Por ejemplo: el promedio
    d_int = None
    if duracion == '':
        d_int = 0
    else:
        d_int = duracion[:-4]
    return d_int
def linea_to_serie(linea, v_genero):
    linea = linea.split('|')
    link = linea[0]
    title = linea[1]
    runtime_se = linea[2]
    certif = linea[3]
    runtime_ep = int(duracion_to_int(linea[4]))
    genre = genre_to_int(linea[5], v_genero)
    rating = float(linea[6].replace(',','.'))
    overv = linea[7]
    star = linea[8]
    start2 = linea[9]
    start3 = linea[10]
    start4 = linea[11]
    votes = int(linea[12])
    reg = Serie(link, title, runtime_se, certif, runtime_ep, genre, rating, overv, star,start2,start3,start4, votes)
    return reg
def leer_series(nombre_archivo, v_series, v_genero):
    m = open(nombre_archivo, 'rt')
    es_encabezado = True
    for linea in m:
        if not es_encabezado:
            if linea[-1] == '\n':
                linea = linea[:-1]
            serie = linea_to_serie(linea, v_genero)
            if serie.runtime_episode != 0:
                add_in_order(serie, v_series)
        else:
            es_encabezado = False
    m.close()
def filtroMinuto(a,b,vect,fdTxt):
    #New Vector
    vector3 = []
    suma = 0
    if b < a:
        b,a = a,b
    for i in vect:
        if a < i.runtime_episode < b:
            vector3.append(i)
            print(i.str())
            suma += i.runtime_episode
    print(f'el promedio de su filtro fue de {promedio(suma,len(vector3))}')
    continuar = int(input('deseas guardar este filtro en un archivo txt si(1) no(2): '))
    if continuar == 1:
        writeTxT(vector3,fdTxt)
        print(f'se guardo con exito en {fdTxt}')
    else:
        print('usted decidio no guardar el presente filtro')
def promedio(sum,total):
    if total != 0:
        return sum/total
    return 'No hubo resultados'
def writeTxT(vect,fd):
    m = open(fd,'w')
    for i in vect:
        m.write(str(i)+'\n')
    m.close()
def vectorConteos(vect_genero:list, vectSeries:list):
    vectorConteo = [0]* (len(vect_genero)-1)
    for i in vectSeries:
        if i.genre != None:
            vectorConteo[i.genre] += 1
    return vectorConteo
def genero_int_str(vect_genero:list, vectorConteo):
    for i in range(len(vectorConteo)):
        print(f'hubo en el genero {vect_genero[i]}: {vectorConteo[i]}')
def writeBynari(fd,vect:list):
    newList = []
    with open(fd,'wb') as m:
        for i in vect:
            newList.append(i)
        if len(newList) > 0:
            pickle.dump(newList,m)
        m.close()
def readBinary(fd):
    if not os.path.exists(fd):
        print('no existe el archivo')
        return None
    else:
        with open(fd,'rb') as m:
            n = pickle.load(m)
        m.close()
        return n
def busquedaTitulo(vect_series,tit):
    bandera = True
    for i in vect_series:
        if tit == i.title:
            i.votes += 1
            print('Se encontro resultado')
            print(i)
            bandera = False
    if bandera:
        print('No se encontro')