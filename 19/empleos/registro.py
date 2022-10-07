import random


class Empleo:
    def __init__(self,ID:int,descripcion:str,monto:int,ciudad:int,tipo:int) -> None:
        self.ID = ID
        self.descripcion = descripcion
        self.monto = monto
        self.ciudad = ciudad
        self.tipo = tipo
    def __str__(self) -> str:
        return f'ID: {self.ID}, descripcion: {self.descripcion}, monto: {self.monto}, ciudad: {self.ciudad}, tipo de empleo: {self.tipo}'
def cargar(vect:list,n):
    dim = len(vect)
    for i in range(n):
        id = i + dim + 1
        description = random.choice(['a','b','c'])+str(i + dim + 1)
        monto = random.randint(5000,15000)
        ciudad = random.randint(0,29)
        tipo = random.randint(0,19)
        vect.append(Empleo(id,description,monto,ciudad,tipo))
    inserccion(vect)
    printVect(vect)
def printVect(vect:list):
    for i in vect:
        if 0 <= i.ciudad <= 10:
            print(i)
def inserccion(vect:list):
    pos = 0
    aux = 0
    for i in range(len(vect)):
        pos = i
        aux = vect[i]
        while pos > 0 and vect[pos-1].ID > aux.ID:
            vect[pos] = vect[pos-1]
            pos -= 1
        vect[pos]= aux