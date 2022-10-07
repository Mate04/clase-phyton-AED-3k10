import random
class Venta:
    def __init__(self,numeroTicket:int,nombreDelCliente:str,importe:int,codigoVenderor:int,codigoProducto:int):
        self.numeroTicket = numeroTicket
        self.nombreDelCliente = nombreDelCliente
        self.importe = importe
        self.codigoVenderor = codigoVenderor
        self.codigoProducto = codigoProducto
    def __str__(self):
        return f'numero de ticket: {self.numeroTicket}, nombre del cliente es {self.nombreDelCliente}, importe {self.importe}, codigo de Vendedor: {self.codigoVenderor}, codigo de Producto {self.codigoProducto}'
def cargar(vect:list,n):
    dim = len(vect)
    for i in range(n):
        nombre = random.choice(["Mateo", "Marti","Lucacho","Igna","Mati"])+" "+random.choice(['Maldonado','Franco','Loyola','Cuello','Arrigonni','Sciarra'])
        importe = random.randint(90000,10000000)
        codigoVendedor = random.randint(1,13)
        codigoProducto = random.randint(0,7)
        vect.append(Venta(i+1+dim,nombre,importe,codigoVendedor,codigoProducto))
def printVect(vect:list):
    for i in range(len(vect)):
        print(vect[i])
def validarNumerodeCarga(n):
    while n <= 0:
        n = int(input('ingrese un numero valido: '))
    return n
def may_to_min(vect:list):
    for i in range(len(vect)-1):
        for j in range(i+1, len(vect)):
            if vect[i].importe < vect[j].importe:
                vect[i].importe, vect[j].importe = vect[j].importe, vect[i].importe
    return vect
def punto2(vect:list,x,y):
    vect = may_to_min(vect)
    for i in range(len(vect)):
        if x < vect[i].importe < y:
            print(f'Nombre del Cliente {vect[i].nombreDelCliente}, el importe es {vect[i].importe}, codigo del producto {vect[i].codigoProducto}')
def contador(vect:list):
    conteo = [0]*8
    for i in range(len(vect)):
        conteo[vect[i].codigoProducto-1] += vect[i].importe
    return conteo
def punto3(vect):
    par = impar = 0
    conteo = contador(vect)
    for i in range(len(conteo)):
        print(f'La clase {i+1} recaudo {conteo[i]}')
        if (i+1) % 2 == 0:
            par += conteo[i]
        else:
            impar += conteo[i]
    if par > impar:
        print('se recaudo mas con el producto par')
    elif impar > par:
        print('se recaudo mas con el producto impar')
    else:
        print('El producto par e impar son lo mismo')
def punto4(vect):
    vect = may_to_min(vect)
    print(vect[-1])
def punto5(vect:list,t:int):
    bandera = True
    for i in range(len(vect)):
        if vect[i].numeroTicket == t and (1 <= vect[i].codigoVenderor <= 5):
            print(vect[i])
            bandera = False
    return bandera