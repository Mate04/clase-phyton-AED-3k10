from modulo_peaje import *
import random
import os.path
import pickle
def validar():
    n=int(input("Ingrese un num para el arreglo:"))
    while n<=0:
        n=int(input("Ingrese un valor valido:"))
    return n
def cargar_arreglo():
    num_i=random.randint(10,50)
    nom=random.choice(["Autopista Carlos Paz.", "Córdoba acceso norte.","Las Tilas.","Vilaa Serranita."])
    monto=random.randint(100,1000)
    patente=random.randint(10,40)
    hora=random.randint(00,23)
    return Peaje(num_i,nom,monto,patente,hora)
def crear_arreglo(vec,n):
    for i in range(n):
        vec.append(cargar_arreglo())

def mostrar_vec(vec):
    for i in range(len(vec)):
        print(to_str(vec[i]))


def ordenar(vec,m):
    n=len(vec)
    for i in range(n-1):
        #if vec[i].monto<m:
            for j in range(i+1,n):
                    if vec[i].num_i>vec[j].num_i:
                        vec[i],vec[j]=vec[j],vec[i]
    for i in range(n):
        if vec[i].monto<m:
            print(to_str(vec[i]))

#def punto_tres(vec,m):
    #for i in range(len(vec)):
        #if vec[i].monto<m:
            #print(to_str(vec[i]))
def acumuladores(vec):
    acumuladores=[0]*24
    for i in range(len(vec)):
        acumuladores[vec[i].hora]+=vec[i].monto
    for i in range(len(acumuladores)):
        #TODO: i va emular las horas, y el siguien
        #ToDO: condicional nos dice si la hora (i) esta
        #TODO: entre las 21 a 23 horas, 
        #TODO: o esta entre las 1 a 5 horas 
        if 20<i<24 or 0<i<6:
            #TODO: acumuladores[i] es el monto en si
            if acumuladores[i]!=0:
                print(f"Hora {i}",acumuladores[i])
    return acumuladores
def crear_archivo(vec,id):
    x_nom=input("Ingrese el nombre del archivo a crear:")
    archivo=open(x_nom,"wb")
    for i in (vec):
        if i.num_i==id:
            pickle.dump(i,archivo)
    print("se creo el archivo:",x_nom,"Con el num de id:",id)
    archivo.close()
def mostrar(x_nom):
    if not os.path.exists(x_nom):
        print("no existe el archivo")
        return
    else:
        archivo=open(x_nom,"rb")
        m=os.path.getsize(x_nom)
        while archivo.tell()<m:
            res=pickle.load(archivo)
            print(to_str(res))
        archivo.close()
def busqueda(p,h,vec):
    for i in range(len(vec)):
        if vec[i].patente==p:
            if vec[i].hora==h:
                print(vec[i].nom)
                return vec[i].nom
    print("no existe")
def mayuscula(cadena):
    mayuscula="ABCDEFGHIJKLMNÑOPQRSTUWXYZ"
    return cadena in mayuscula
#Tome la cadena retornada en el punto 7 anterior, y determine cuántas palabras de esa cadena contienen al menos una letra mayúscula.
# Puede considerar que la cadena termina siempre con un punto, y que las palabras se separan entre ellas con un (y solo un) espacio en blanco.
# La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella.
def punto_ocho(hola):
    cont=0
    for c in hola:
        if c not in " . ":
            if mayuscula(c):
                cont+=1
    print("Hubo",cont,"mayusculas")


def main():
    op=-1
    vec=[]
    bandera=False
    mateo=False
    hola=None
    while op!=100000000:
        op=int(input("ingrese una opcion:"))
        if op==1:
            n=validar()
            crear_arreglo(vec,n)

            bandera=True
        if op!=1 and bandera==False:
            print("No se cargo el vector")
        else:
            if op==2:
                mostrar_vec(vec)
            if op==3:
                m=int(input("Ingrese un importe a comparar:"))
                ordenar(vec,m)
                #mostrar_vec(vec)
                #punto_tres(vec,m)
            if op==4:
                acumuladores(vec)
            if op==5:
                id=int(input("Ingrese un num de identificacion:"))
                crear_archivo(vec,id)
            if op==6:
                x_nom=input("ingrese el nom a buscar.")
                mostrar(x_nom)
            if op==7:
                h=int(input("ingrse una hora a buscar"))
                p=int(input("ingrese una patente a buscar:"))
                hola=busqueda(p,h,vec)
                mateo=True
            if op==8 and mateo:
                punto_ocho(hola)

if __name__ == '__main__':
    main()
