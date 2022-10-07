import pickle
import random
from registro import Registro

def menu():
    print('='*20)
    return int(input('opcion 1: cargar vector\nopcion 2: punto 2\nopcion 3: buscar id\nopcion 4: busqueda de precio\nopcion 6: lectura del archivo binario\nopcion 8: mostrar del archivo binario solo id, descripcion, precio\nopcion 0: salir\nopcion: '))
def cargar(vect:list,n):
    dimentions = len(vect)
    for i in range(n):
        id = dimentions + i+1
        descripcion = random.choice(['a', 'b', 'c'])+str(i)
        precio = random.randint(1000,10000000)
        lugar = random.randint(0,24)
        articulo = random.randint(0,29)
        vect.append(Registro(id,descripcion,precio,lugar,articulo))
def printVect(vect:list):
    for i in vect:
        print(i)
def printVectPunto2(vect:list,p):
    for i in vect:
        if p != i.lugar:
            print(i)

def inserccion(vect:list):
    pos = 0
    aux = 0
    for i in range(len(vect)):
        pos = i
        aux = vect[i]
        while pos >0 and vect[pos-1].id < aux.id:
            vect[pos] = vect[pos-1]
            pos -= 1
        vect[pos] = aux
def busquedaBinaria(vect:list,num:int):
    dimension = len(vect)
    cont = 0
    inf = 0
    sup = dimension
    while inf <= sup and cont < dimension:
        mitad = (inf+sup)//2
        if vect[mitad].id == num:
            return mitad
        elif vect[mitad].id < num:
            sup = mitad
            mitad = (inf+sup)//2
        elif vect[mitad].id > num:
            inf = mitad
            mitad = (inf+sup)//2
        cont += 1
    return None
def busquedaBinaria2(vect:list,num:int):
    dimension = len(vect)
    cont = 0
    inf = 0
    sup = dimension
    while inf <= sup and cont < dimension:
        mitad = (inf+sup)//2
        if vect[mitad].precio == num:
            return mitad
        elif vect[mitad].precio < num:
            sup = mitad
            mitad = (inf+sup)//2
        elif vect[mitad].precio > num:
            inf = mitad
            mitad = (inf+sup)//2
        cont += 1
    return None
def punto3(vect:list):
    id = int(input('que id desea buscar: '))
    x = busquedaBinaria(vect,id)
    if x != None:
        print(vect[x])
    else:
        print(f'el id {id}, no encontro!!')
def punto4(vect:list):
    precio = int(input('que precio desea buscar: '))
    x = busquedaBinaria2(vect,precio)
    if x != None:
        print(f'id: {vect[x].id}, descripcion: {vect[x].descripcion}')
    else:
        print('no se encontro el precio que solicito!!!')
def creacionArchivoBinario(fb,vect):
    with open(fb,'wb') as m:
        pickle.dump(vect,m)
    m.close()
def lecturaArchivoBinario(fb,vect):
    with open(fb,'rb') as m:
        vect = pickle.load(m)
        m.close()
    for i in vect:
        print(i)
    return vect
def lecturaArchivoBinario2(fb):
    with open(fb,'rb') as m:
        vect = pickle.load(m)
        m.close()
    for i in vect:
        print(f'id: {i.id}, descripcion: {i.descripcion}, precio {i.precio}')