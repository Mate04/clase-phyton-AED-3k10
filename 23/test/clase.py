import random,string
vector = []
class Obras:
    def __init__(self,num_i,nom,origen,precio):
        self.num_i=num_i
        self.nom=nom
        self.origen=origen
        self.precio=precio
    def __str__(self) -> str:
        return f"id {self.num_i}, nombre {self.nom}, origen: {self.origen}, precio {self.precio}"
def printVect(vect):
    for i in vect:
        print(i)
def crear(vector, n):
    dim = len(vector)
    for i in range(n):
        id = random.randint(1,100000)
        nom = ''.join(random.choice(string.ascii_letters)for i in range(random.randint(5,8)))
        origen = random.randint(1,49)
        precio = random.randint(100,1000000)
        vector.append(Obras(id,nom,origen,precio))
    printVect(vector)

crear(vector,5)
def ordenar(vect):
    aux = vect[:]
    vect = []
    for i in aux:
        add_in_orden(vect,i)
    printVect(vect)
def add_in_orden(vect:list,clase:classmethod):
    dim = len(vect)
    izq = 0
    der = dim-1
    pos = dim
    while izq <= der:
        mitad = (der+izq)//2
        if vect[mitad].num_i == clase.num_i:
            pos = mitad
            break
        elif vect[mitad].num_i > clase.num_i:
            der = mitad - 1
        else:
            izq = mitad + 1
    if izq > der:
        pos = izq
    vect[pos:pos] = [clase]
print('='*20)
ordenar(vector)