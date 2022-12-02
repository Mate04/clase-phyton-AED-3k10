import random
import string


class Dato:
    def __init__(self,codigo,descripcion,precio,tipoPoliza,formaPago) -> None:
        self.id = codigo
        self.descricion = descripcion
        self.precio = precio
        self.tipoPoliza = tipoPoliza
        self.formaPago = formaPago
    def __str__(self) -> str:
        return f'ID: {self.id}, descripcion {self.descricion}, precio {self.precio}, tipo de poliza {self.tipoPoliza}, forma de pago {self.formaPago}'
def cargar(vect:list,n):
    dim = len(vect)
    n = validar(n)
    for i in range(n):
        id = i + dim + 1
        descripcion = ''.join(random.choice(string.ascii_letters)for i in range(random.randint(6,12)))
        precio = random.randint(5000,10000)
        tipo = validar(random.randint(0,19),0,19)
        formaPago = validar(random.randint(1,5),1,5)
        add_in_ord(vect,Dato(id,descripcion,precio,tipo,formaPago))
    printVect(vect)
def add_in_ord(vect:list,clase:classmethod):
    dim = len(vect)
    izq = 0
    der = dim-1
    pos = dim
    while izq <= der:
        mitad = (der+izq)//2
        if vect[mitad].descricion == clase.descricion:
            pos = mitad
            break
        elif vect[mitad].descricion < clase.descricion:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    vect[pos:pos] = [clase]
def printVect(vect):
    for i in vect:
        print(i)
def validar(n,min=0,max=0):
    if min == 0 and max == 0:
        while n < 1:
            n = int(input('porfavor ingrese un numero mayor a 0: ')) 
        return n
    else:
        while min > n or n > max:
            n  = int(input(f'porfavor elija un numero entre {min} y {max}: '))
        return n
