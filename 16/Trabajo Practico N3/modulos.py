import string, random
from prettytable import PrettyTable

class Proyecto():
    def __init__(self,n_proy,tit,act,ln,n_cod,año):
        self.n_proy = n_proy #Numero de proyecto
        self.tit = tit #Titulo
        self.act = act #Fecha de actividad
        self.ln = ln #Lenguaje
        self.n_cod = n_cod#Cantidad de lineas de codigo.
        self.año = año
    def getDatail(self): #Retorna un arreglo de todos los atributos que recibe la clases
        return [self.n_proy,self.tit,self.act,self.ln,self.n_cod,self.año]

def menu():
    print ("")
    print("1 - Opcion ")
    print("2 - Opcion ")
    print("3 - Opcion ")
    print('4 - Opcion ')
    print("5 - Opc")
    print('6 - Opcion filtro de lenguanje')
    print("7 - Opc")
    print("8 - Salir")
    print("")
    opcion=int(input('Elija una opcion: '))
    while opcion < 1 or opcion > 8:
      opcion=int(input('Operacion Invalida, elija una opcion: '))
    return opcion

def generar_fecha():
    dia = random.randint(1,31)
    mes = random.randint(1,12)
    año = random.randint(2000,2022)
    while mes == 2 and dia == (29 or 30 or 31): #Si el mes es febrero 
        dia = random.randint(1,29)
    fecha = str(dia)+"-"+str(mes)+"-"+str(año)
    return fecha,año

def generar_titulo():
    titulo = ""
    for i in range(5):
        letra = random.choice(string.ascii_letters) 
        titulo += letra
    return titulo

def cargar_datos(proyectos):
    n = int(input('Ingrese cuantos proyecto quiere cargar: '))
    for i in range(n):
        fecha = generar_fecha()
        titulo = generar_titulo()
        fecha_actualizacion = fecha[0]
        lenguaje = random.randint(0,9)
        cant_lineas_codigo = random.randint(30,1000)
        año = fecha[1]
        proyectos.append(Proyecto(i+ len(proyectos),titulo,fecha_actualizacion,lenguaje,cant_lineas_codigo,año))
        
def to_string(vector):
    lenguajes = ("Python","Java","C++","JavaScript","Shell","HTML","Ruby","Swift","C#","VB","Go")
    r = ''
    r += '{:<20}'.format('Nro de proyecto: ' + str(vector.n_proy))
    r += '{:<20}'.format('Titulo: ' + str(vector.tit))
    r += '{:<35}'.format('Fecha de actualizacion: ' + str(vector.act))
    r += '{:<25}'.format('Lenguaje: ' + str(lenguajes[vector.ln]))
    r += '{:<10}'.format('Nro lineas de codigo: ' + str(vector.n_cod))
    return r

def mostrar(vec):
    n = len(vec)
    for i in range(n):
        print(to_string(vec[i]))
    
def sort_proy(proyectos):
    n = len(proyectos)
    proyectos_ord_tit = proyectos[:]
    for i in range(n-1):
        for j in range(i+1,n):
            if proyectos_ord_tit[i].tit > proyectos_ord_tit[j].tit:
                proyectos_ord_tit[i], proyectos_ord_tit[j] = proyectos_ord_tit[j], proyectos_ord_tit[i]
    return proyectos_ord_tit

def actualizar(x, proyectos):
    n = len(proyectos)
    for i in range(n):
        for j in range(n):
            pass

def search_binario(proyectos,x):
    posicion = None
    izq = 0
    der = len(proyectos)-1
    while izq <= der:
        c = (izq + der) // 2
        if x == proyectos[c].n_proy:
            posicion= c 
            break
        if x < proyectos[c].n_proy:
            der = c-1
        else :
            izq = c +1
    return posicion

def validacion(i,fecha,f):
    while fecha < i or fecha > f:
        fecha = int(input("Invalido, ingrese de vuelta:"))
    return fecha

def punto3(proyecto):
    x=int(input('elija el numero de un proyecto'))
    busqueda = search_binario(proyecto,x)
    if busqueda != None:
        print('Se encontro El proyecto')
        print('1 - Modificar la fecha de actualizacion DD-MM-YYYY')
        print('2 - Modificar cantidad de lineas de codigo')
        print('0 - Salir')
        l = int(input('Que quiere modificar?: '))
        while l < 1 or l> 2:
            l=int(input('Invalido, Que quiere modificar?: '))
        if l == 1 :
            dia = int(input("Elija dia: "))
            dia = validacion(1, dia, 31)
            mes = int(input("Elija Mes: "))
            mes = validacion(1, mes, 12)
            años = int(input ("Elija Año: "))
            años = validacion(2000, años, 2022)
            proyecto[busqueda].año = años
            proyecto[busqueda].act = str(dia)+"-"+str(mes)+"-"+str(años)
        if l == 2 :
            proyecto[busqueda].n_cod=int(input('Ingrese la cantidad de lineas de codigo actual '))
    else:
        print('El proyecto no existe')

def punto4(proyectos):
  lenguajes = ("Python","Java","C++","JavaScript","Shell","HTML","Ruby","Swift","C#","VB","Go")
  cont_ln = [0] * 10
  for i in range(len(proyectos)):
    cont = proyectos[i].ln
    cont_ln[cont] += 1
  for j in range(len(cont_ln)):
    r = " "
    r += '{:<20}'.format('Lenguaje: ' + lenguajes[j])
    r += '{:<20}'.format('Cant: ' + str(cont_ln[j]))
    print(r)

def buscar_mayor(vec):
    may = vec[0]
    for i in range(len(vec)):
        if vec[i] > may:
            may = vec[i]
    return may
def mostrar_años_con_mas_proy(may,vec):
    for i in range(len(vec)):
        if vec[i] == may:
            print("Año: ",i+2000)


def punto6(lenguaje, vector):
    lenguajes = ("Python","Java","C++","JavaScript","Shell","HTML","Ruby","Swift","C#","VB","Go")
    ln_filtro = []
    if lenguaje >= 0 and lenguaje <= 10:
        for i in range(len(vector)):
            if vector[i].ln == lenguaje:
                ln_filtro.append(vector[i])
        if len(ln_filtro) != 0:
            ln_filtro = ordenar_min_to_max(ln_filtro)
            mostrar(ln_filtro)
        else: 
            print(f'No se encotro el lenguaje {lenguajes[lenguaje]}')
    else:
        print(f'opcion invalidad ya que el numero que elijio {lenguaje} no existe ')

def contar_por_año(proy):
    años = [0]*23
    for i in range(len(proy)):
        años[(proy[i].año % 2000)] += 1
    return años

def mostrar_proy_por_año(años):
    for i in range(len(años)):
        if años[i] != 0:
            print("Año:",i+2000,",Cantidad de proyectos:",años[i])

def ordenar_min_to_max(vect_filtrado):
    for i in range(len(vect_filtrado)):
        for m in range(len(vect_filtrado)):
            if vect_filtrado[i].n_proy < vect_filtrado[m].n_proy:
                vect_filtrado[i], vect_filtrado[m] = vect_filtrado[m],vect_filtrado[i]
    return vect_filtrado