import random
from modulo import *


class venta:
    def __init__(self,numeroFactura,importeDeLaFactura,tipo:str,apellido,perfumeVendido):
        self.numeroFactura = numeroFactura
        self.importeDeLaFactura = importeDeLaFactura
        self.tipo = tipo
        self.apellido = apellido
        self.perfumeVendido = perfumeVendido
    def __str__(self):
        return "Numero de factura "+str(self.numeroFactura)+" importe de factura "+str(self.importeDeLaFactura)+" tipo: "+str(self.tipo)+" apellido: "+str(self.apellido)+" tipo de perfume: "+str(self.perfumeVendido)

def printVector(vect):
    for i in range(len(vect)):
        print(vect[i])
def cargar(vect):
    n = len(vect)
    for i in range(int(input("cuantas ventas quiere procesar: "))):
        importeDeLaFactura = random.randint(50,10000)
        tipo = random.choice(["A","B","C"])
        apellido = random.choice(["Maldonado","Franco","Loyola"])
        perfumeVendido = random.randint(1,17)
        vect.append(venta(i+1+n,importeDeLaFactura,tipo,apellido,perfumeVendido))

def max_to_min(vect):
    for i in range(len(vect)-1):
        for j in range(i+1,len(vect)):
            if int(vect[i].numeroFactura) < int(vect[j].numeroFactura):
                vect[i],vect[j]=vect[j],vect[i]
    return vect
def mostrar(vect,x,t):
    vect = max_to_min(vect)
    for i in range(len(vect)):
        if vect[i].importeDeLaFactura > x and vect[i].importeDeLaFactura != t:
            print(vect[i])

def contador(vect):
    vectContador = [0]*17
    for i in range(len(vect)):
        vectContador[vect[i].perfumeVendido-1] += vect[i].importeDeLaFactura
    return vectContador

def punto3(vect):
    vectorConteo = contador(vect)
    z = int(input("que tipo de perfume quiere saber que importe tuvo"))
    print(vectorConteo[z-1])

def punto5(vect,p):
    for i in range(vect):
        if vect[i].numeroFactura1 == len(vect) and vect[i].importeDeLaFactura < p:
            print("si existe")
        else:
            print("no existe")

def main():
    op = True
    Ventas = []
    while op != 0:
        op = int(input("opcion a elegir/ 1-cargar / 2- punto 2\n"))
        if op == 1:
            cargar(Ventas)
            printVector(Ventas)
        if op == 2:
            mostrar(Ventas,int(input("que filtro quiere agregar para que 'x' sea mayor a importes: ")),int(input("valor de t: ")))
        if op == 3:
            punto3(Ventas)
        if op == 5:
            punto5(Ventas,int(input("p que valor toma: ")))
if __name__ == "__main__":
    main()
