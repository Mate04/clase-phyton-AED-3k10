import random, string


class contenido:
    def __init__(self,codigo:int,nombre:str,tipo:int,calificacion:int,reproducciones:int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.calificacion = calificacion
        self.reproducciones = reproducciones
    def __str__(self) -> str:
        return f'codigo: {self.codigo}, nombre: {self.nombre}, tipo: {self.tipo}, calificacion: {self.calificacion}, reproducciones: {self.reproducciones}'
def cargar(vect:list,n:int):
    dim = len(vect)
    for i in range(n):
        codigo = i + dim + 1
        nombre = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5,10)))
        tipo = validar(1,15,random.randint(1,15))
        calificacion = validar(0,12,random.randint(0,12))
        cantidad = random.randint(5000,35000)
        add_in_orden(vect,contenido(codigo,nombre,tipo,calificacion,cantidad))
    printVect(vect)
def add_in_orden(vect:list,clase:classmethod):
    dim = len(vect)
    izq = 0
    der = dim-1
    pos = dim
    while izq <= der:
        mitad = (der+izq)//2
        if vect[mitad].codigo == clase.codigo:
            pos = mitad
            break
        elif vect[mitad].codigo < clase.codigo:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    vect[pos:pos] = [clase]
def printVect(vect:list):
    for i in vect:
        print(i)

def validar(min,max,n):
    while n < min or n > max:
        n = int(input(f'elija un numero entre {min} y {max}: '))
    return n
