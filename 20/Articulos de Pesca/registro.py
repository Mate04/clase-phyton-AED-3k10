

import random
import string


class articulo:
    def __init__(self,id,descripcion,precio,lugar,tipo) -> None:
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.lugar = lugar
        self.tipo = tipo
    def __str__(self) -> str:
        return f'identificacion {self.id}, descripcion {self.descripcion}, precio: {self.precio}, lugar: {self.lugar}, tipo: {self.tipo}'
"""
Una empresa de venta de artículos de pesca deportiva mantiene información sobre los distintos artículos que tiene a la venta. Por cada artículo se registran los datos siguientes: número de identificación (un entero), descripción del artículo (una cadena), precio de venta, lugar de origen del artículo (un valor entre 0 y 24 incluidos, por ejemplo: 0: Argentina, 1: Canadá, etc.) y tipo de artículo (un número entero entre 0 y 29 incluidos, para indicar (por ejemplo): 0: anzuelo, 1: caña, etc.) Se pide definir un tipo registro Articulo con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:
"""
def cargar(vect,n):
    dim = len(vect)
    n = validar(n)
    for i in range(n):
        id = i + dim + 1
        descripcion = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5,12)))
        venta = random.randint(5000,100000)
        lugar = validar(random.randint(0,24),0,24)
        tipo = validar(random.randint(0,29),0,29)
        add_in_orden(vect,articulo(id,descripcion,venta,lugar,tipo))
    printVect(vect)
def add_in_orden(vect,clase):
    dim = len(vect)
    izq = 0
    der = dim-1
    pos = dim
    while izq <= der:
        mitad = (der+izq)//2
        if vect[mitad].id == clase.id:
            pos = mitad
            break
        elif vect[mitad].id > clase.id:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    vect[pos:pos] = [clase]

def validar(n,min=0,max=0):
    if min == 0 and max ==0:
        while n < 1:
            n = int(input('ingresa un numero mayor a 0: '))
    else:
        while min > n or n > max:
            n = int(input(f'porfavor ingrese un numero entre {min} y {max}: '))
    return n
def printVect(vect):
    for i in vect:
        print(i)