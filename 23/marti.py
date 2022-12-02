import random
#Creamos la clase, que su unico parametro es el de ID
class Id:
    def __init__(self,id) -> None:
        self.id = id
    def __str__(self) -> str:
        return f'id: {self.id}'
#Cargamos el vector
def cargarVector(vect:list,n):
    for i in range(n):
        id = random.randint(1,100000)
        vect.append(Id(id))
    #Mostramos el vector Desordenado
    for i in vect:
        print(i)
    #Creamos una funcion de re-ordenamiento, su parametro es el vector, y esta funcion retorna
    #el vector ya ordenado por eso lo igualamos al vector original
    vect = re_ordenamiento(vect)
    #Mostramos ahora si el vector ordenado
    print('Ordenamiento menor a mayor: ')
    for i in vect:
        print(i)
def add_in_ord(vect,clase):
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
def re_ordenamiento(vect):
    #Creamos un vector paralelo, 
    #copiando lo mismo elementos del vector original
    #lo hacemos con el siguiente comando 
    aux = vect[:]
    #Vaciamos el vector original,
    # pero recorda que queda los elementos en el vector aux
    vect = []
    #hacemos el recorrido del vector aux
    for clase in aux:
        #llamamos a la funcion tipica de add_in_ord, su primer parametro es el vector 
        #original recordar que el vector esta vacio. Y el segundo parametro es elemento 
        #de aux, en este caso lo llamamos 'clase'
        add_in_ord(vect,clase)
    #Una vez ordenado todo, devolvemos el vector, esto lo tenemos q guardar en un vector
    #puede ser tanto el mismo vector, como otro nuevo, en este caso linea 18
    #lo guardamos en el mismo vector
    return vect
vector = []
cargarVector(vector,5)