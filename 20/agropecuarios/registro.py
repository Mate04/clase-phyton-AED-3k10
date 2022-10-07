import random
import string


class operacion:
    def __init__(self,ID:int,descrip:str,importe:float,operacion:int,campo:int) -> None:
        self.id = ID
        self.descrip = descrip
        self.importe = importe
        self.operacion = operacion
        self.campo = campo
    def __str__(self) -> str:
        return f'ID {self.id}, descripcion {self.descrip}, importe {self.importe}, operacion {self.descrip}, numero de campo {self.campo}'
def cargar(vect:list,n:int):
    dim = len(vect)
    for i in range(n):
        id = i + dim + 1
        descripcion = ''.join(random.choice(string.ascii_letters)for i in range(random.randint(5,8)))
        importe = random.uniform(50000,1000000)
        operacionl = random.randint(1,15)
        campo = random.randint(0,19)
        add_in_ord(vect,operacion(id,descripcion,importe,operacionl,campo))
    printVect(vect)
def add_in_ord(vect:list,clase:classmethod):
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
def printVect(vect):
    for i in vect:
        print(i)