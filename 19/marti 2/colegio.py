from modulo_colegio import *
import random
import pickle
import os.path
"""Por cada miembro se registran los campos siguientes: número de dni del profesional (un número entero), nombre del profesional (una cadena),
 importe que paga al colegio por mes, tipo de afiliación (un valor entre 0 y 4 incluidos, por ejemplo de la forma 0: vitalicio, 1: transitorio,
 2: indirecto, etc.) y un número que identifica el tipo de trabajo que desempeña (un número entero entre 0 y 14 incluidos, para indicar (por ejemplo):
  0: empleado, 1: jefe o director, 2: administrativo, etc.) Se pide definir un tipo registro Profesional con los campos que se indicaron, y un programa
   completo con menú de opciones para hacer lo siguiente:"""
def validar(n):
    while n<=0:
        n=int(input("ingrese un num valido"))
def cargar_vector(vec,n):
    for i in range(n):
        dni=random.randint(45000,46000)
        Nombre=random.choice(["Sandra","Bad Bunny","Maria","Trueno","Nicky"])
        importe=random.uniform(100,1000)
        tipo=random.randint(0,4)
        numero=random.randint(0,14)
        profe=Profesionales(dni,Nombre,importe,tipo,numero)
        add_in_order(vec,profe)
    return vec
def mostrar_vec(vec):
    for profe in vec:
        print(profe)
#punto tres
# Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado).
# Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que tiene el importe desactualizado,
# si es menor a un valor imp (tambien cargado por teclado)
def buscar(vec,doc):
    n=len(vec)
    izq=0
    der=n-1
    pos=None
    while izq<=der:
        c=(izq+der)//2
        if vec[c].dni==doc:
            pos=c
            break
        elif doc<vec[c].dni:
            der=c-1
        else:
            izq=c+1
    if pos==None:
        print("no se encontro")
    else:
        print("El importe original es:",vec[pos].importe)
        importe=int(input("Ingrese un nuevo importe: "))
        if vec[pos].importe<importe:
            vec[pos].importe=importe
        print(vec[pos])
#punto cuatro:
"""A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo tipo de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual 
sea mayor a un valor x que se carga por teclado."""
def crear_archivo(fd,vec,x):
    m=open(fd,"wb")
    new_list=[]
    for profe in vec:
        if (profe.tipo==3 or profe.tipo==4 or profe.tipo==5) and profe.importe>x:
            new_list.append(profe)
    pickle.dump(new_list,m)
    m.close()
    print("se creo el archivo:",fd,"con el importe mayor:",x)
def mostrar_archivo(fd):
    profe=[]
    if not os.path.exists(fd):
        print("no existe el archivo")
    else:
        m=open(fd,"rb")
        t=os.path.getsize(fd)
        while m.tell()<t:
            profe=pickle.load(m)
            #print(profe)  LO QUE NO HAY QUE HACER XQ MATEO LO DICE
        for i in profe:
            print(i)
        m.close()
#punto seis
"""Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar nom por teclado). 
Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que 
coincida con el patrón pedido."""
def punto_seis(vec,nom):
    busqueda=None
    for i in range(len(vec)):
        if vec[i].nombre==nom:
            busqueda=vec[i].nombre
            return busqueda
    return busqueda
#PUNTO SIETE
"""Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación por cada posible tipo de trabajo
 (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de 0.
"""
def crear_matriz(vec):
    matriz=[[0]*5 for i in range(15)]
    for i in vec:
        matriz[i.trabajo][i.tipo]+=1
    return matriz
def mostrar_m(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]!=0:
                print(f'la matriz fila: {i} columna {j}:',matriz[i][j])
def main():
    vec=[]
    fd="profe.dat"
    op=-1
    while op!=1000:
        op=int(input("ingrese una opcion:"))
        if op==1:
            n=int(input("ingrese un num a cargar:"))
            validar(n)
            vec=cargar_vector(vec,n)
        elif op==2:
            mostrar_vec(vec)
        if op==3:
            doc=int(input("ingrese un num de doc:"))
            buscar(vec,doc)
        elif op==4:
            x=float(input("ingrese un importe:"))
            crear_archivo(fd,vec,x)
        elif op==5:
            mostrar_archivo(fd)
        elif op==6:
            nom=input("ingrese nombre por teclado:")
            nuevo=punto_seis(vec,nom)
            if nom==None:
                print("no se encontro")
            else:
                for i in vec:
                    print(i)
        elif op==7:
            matriz=crear_matriz(vec)
            mostrar_m(matriz)


if __name__ == '__main__':
    main()
