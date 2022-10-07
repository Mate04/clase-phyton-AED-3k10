import random
import string

class Trabajo:
    def __init__(self,identificacion,descripcion,tipo,importe,cantidad):
        self.id = identificacion
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.cant = cantidad
    def __str__(self):
        return f'identificacion: {self.id}, Descripcion "{self.descripcion}" , tipo {self.tipo}, importe {self.importe}$, cantidad de trabajadores {self.cant}'
def cargar(vect:list,n):
    k = len(vect)
    for i in range(n):
        descripcion = generadorCaracteres(random.randint(5,16))
        tipoTrabajo = random.randint(0,19)
        importe = random.randint(5000,10000)
        cant = random.randint(1,5)
        vect.append(Trabajo(i+1+k,descripcion,tipoTrabajo,importe,cant))

def generadorCaracteres(aleatorio:int):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(aleatorio))
def printVector(vect:list):
    for i in vect:
        print(i)
def Validar(n:int):
    while n <= 0:
        n = int(input('ingrese un valor mayor a 0: '))
    return n
#! Punto 2
def punto2(vect:list):
    vect = max_to_min(vect)
    total = 0
    for i in vect:
        if i.cant > 3:
            print(i)
            total += i.importe
    print(f'el total recaudado es de {total}')
def max_to_min(vect:list):
    for i in range(len(vect)-1):
        for j in range(i+1,len(vect)):
            vect[i],vect[j] = vect[j],vect[i]
    return vect
#TODO: Punto 3
def punto3(vect:list):
    conteo = contador(vect)
    for i in range(len(conteo)):
        if conteo[i] != 0:
            print(f'La clase {i+1} tuvo un total de {conteo[i]} trabajadores')
def contador(vect:list):
    conteo = [0]*20
    for i in range(len(vect)):
        conteo[vect[i].tipo-1] += vect[i].cant
    return conteo
#todo: Punto 4:
def Punto4(vect):
    sumaPromedio = 0
    for i in vect:
        sumaPromedio += i.importe
    promedi = promedio(sumaPromedio,len(vect))
    for i in vect:
        if i.importe > promedi:
            print(i)
def promedio(a,b):
    if b != 0:
        return a/b
    else:
        return 'no se puede dividir por 0'
def punto5(vect,num,t):
    bandera = True
    for i in vect:
        if i.id == num and i.tipo == t:
            print('se encontro la busqueda\nes la siguiente:')
            print(i)
            bandera = False
            break
    return bandera