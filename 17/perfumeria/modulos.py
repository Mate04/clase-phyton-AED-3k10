import random

class Venta:
    def __init__(self,numeroFactura,importe,tipoFactura,apellido,tipoPerfume):
        self.numeroFactura = numeroFactura
        self.importe = importe
        self.tipoFactura = tipoFactura
        self.apellido = apellido
        self.tipoPerfume = tipoPerfume
    def __str__(self):
        return f'el numero de factura es: {self.numeroFactura}, el importe es {self.importe}, tipo de factura es {self.tipoFactura}, apellido: {self.apellido}, tipo de perfume: {self.tipoPerfume}\n'
#TODO: PUNTO 1
def cargar(vect:list,n):
    for i in range(n):
        importe = validar(random.randrange(0,2000),1,1999)
        tipoFactura = random.choice(['A','B','C','E'])
        apellido = random.choice(['Paredez','Maldonado','Sciarra','Franco','Carlino','Loyola'])
        tipoDePerfume = random.randint(1,17)
        vect.append(Venta(i+1,importe,tipoFactura,apellido,tipoDePerfume))
def Mostrar(vect):
    for i in range(len(vect)):
        print(vect[i])
def validar(num,min,max):
    bandera = True
    while bandera:
        if min < num < max:
            bandera = False
            return num
        else:
            num = int(input('ingrese un numero valido'))
#TODO: Punto 2
def punto2(vect,x,t):
    n = len(vect)
    vect = max_to_min(vect)
    for i in range(n):
        if vect[i].importe > x and vect[i].tipoFactura != t:
            print(vect[i])
def max_to_min(vect):
    for i in range(len(vect)-1):
        for j in range(i+1,len(vect)):
            if vect[i].apellido < vect[j].apellido:
                vect[i],vect[j]=vect[j],vect[i]
    return vect
#TODO: Punto 3
def vectConteo(vect,z):
    conteo = [0]*17
    n = len(vect)
    for i in range(n):
        conteo[vect[i].tipoPerfume-1] += vect[i].importe
    print(f'el tipo {z} recaudo un total de {conteo[z-1]}')
    return conteo
#TODO: Punto 4
def punto4(vect):
    bandera = True
    for i in range(len(vect)):
        if (5 <= vect[i].tipoPerfume <= 12) and (vect[i].tipoFactura == "C"):
            print(f'tipo factura {vect[i].tipoFactura}, importe {vect[i].importe}, el comprador {vect[i].apellido}')
            bandera = False
    return bandera
#TODO: Punto 5
def punto5(vect,n,p):
    bandera = True
    for i in range(len(vect)):
        if vect[i].numeroFactura == n and vect[i].importe < p:
            print(vect[i])
            bandera = False
    return bandera
