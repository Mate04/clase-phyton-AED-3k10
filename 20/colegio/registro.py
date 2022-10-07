import random
import string


class miembro:
    def __init__(self,dni,nombre,importe,afiliacion,numero) -> None:
        self.dni = dni
        self.nombre = nombre
        self.importe = importe
        self.afiliacion = afiliacion
        self.numero = numero
    def __str__(self) -> str:
        return f'DNI: {self.dni}, nombre {self.nombre}, importe: {self.importe}, afiliacion: {self.afiliacion}, numero: {self.numero}'
def cargar(vect:list,n):
    dim = len(vect)
    for i in range(n):
        dni = i + dim + 1
        nombre = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5,10)))
        importe = random.randint(5000,15000)
        afiliacion = random.randint(0,4)
        numero = random.randint(1,15)
        add_in_orden(vect,miembro(dni,nombre,importe,afiliacion,numero))
    printVect(vect)
def add_in_orden(vect,clase):
    dim = len(vect)
    izq = 0
    der = dim-1
    pos = dim
    while izq <= der:
        mitad = (izq+der)//2
        if vect[mitad].dni == clase.dni:
            pos = mitad
            break
        elif vect[mitad].dni < clase.dni:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    vect[pos:pos] = [clase]
def printVect(vect:list):
    for i in vect:
        print(i)