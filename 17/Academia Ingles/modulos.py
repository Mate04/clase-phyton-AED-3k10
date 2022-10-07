import random
from tkinter import N

class Alumno:
    def __init__(self,DNI,nombre,Apellido,DNI_Tutor,importeCuota,nivel):
        self.DNI = DNI
        self.nombre = nombre
        self.Apellido = Apellido
        self.DNI_Tutor = DNI_Tutor
        self.importeCuota = importeCuota
        self.nivel = nivel
    def __str__(self):
        return f'DNI: {self.DNI}, Nombre completo: {self.nombre} {self.Apellido}, DNI Tutor: {self.DNI_Tutor}, importe de cuota {self.importeCuota}, nivel {self.nivel}'

def cargar(vect:list,n):
    for i in range(n):
        DNI = random.randint(20000000,50000000)
        nombre= random.choice(['Mateo','Marti','Mati','Alex','Ignacio'])
        apellido = random.choice(['Maldonado','Franco','Sciarra','Da Silva','Loyola'])
        DNI_Tutor = random.randint(20000000,50000000)
        importe = random.randint(1000,10000)
        nivel = Validar(random.randint(0,12),12,0) 
        vect.append(Alumno(DNI,nombre, apellido, DNI_Tutor, importe,nivel))
def Validar(num, max, min):
    bandera = True
    while bandera:
        if min <= num <= max:
            bandera = False
            return num
        else:
            num = int(input(f'ingrese un numero entre {min} y {max}'))
def validarVector(n):
    while n < 0:
        n=int(input("ingrese un valor correcto mayor 0: "))
    return n
def min_to_max(vect:list):
    for i in range(len(vect)-1):
        for j in range(i+1,len(vect)):
            if vect[i].Apellido > vect[j].Apellido:
                vect[i],vect[j]=vect[j],vect[i]
    return vect
def printVector(vect:list):
    for i in range(len(vect)):
        print(vect[i])
#TODO:punto3
def contador(vect):
    vectContador = [0]*13
    for i in range(len(vect)):
        vectContador[vect[i].nivel-1]+= 1
    punto3(vectContador)
def punto3(vect):
    for i in range(len(vect)):
        if vect[i] != 0:
            print(f'nivel: {i+1}: {vect[i]}')
def punto4(vect, x):
    importeApagar = 0
    for i in range(len(vect)):
        if vect[i].DNI_Tutor == x:
            importeApagar += vect[i].importeCuota
    return importeApagar
def punto5(vect,x):
    noSeEncontro = True
    for i in range(len(vect)):
        if vect[i].Apellido == x:
            noSeEncontro = False
            vect[i].importeCuota -= (vect[i].importeCuota*10)/100
            print(f"al alumno {vect[i].Apellido} se le hace un 10% de descuento quedando con un total de {vect[i].importeCuota}")
            break
        if noSeEncontro:
            print('No se encontro el apellido')