import string
import random

class informacionDeVenta:
    def __init__(self,pasaporte:str,name:str,codeDestino:int,codeClase:int,monto:int):
        self.pasaporte = pasaporte
        self.name = name
        self.codeDestino = codeDestino
        self.codeClase = codeClase
        self.monto = monto
    def __str__(self) -> str:
        return f'el pasaporte del pasajero es: {self.pasaporte}. el nombre del pasajero es {self.name}. el codigo del destino es {self.codeDestino}. el codigo de la clase {self.codeClase}. el codigo de monto {self.monto}'
def cargar(vect:list,n):
    for i in range(n):
        pasaporte = generadorCaracteres(random.randint(5,16))
        name = random.choice(["Mateo","Lucacho","Marti","Mati","Alex","Igna","Colo","Sofi"])+' '+ random.choice(["Maldonado", "Franco", "Sciarra","Da Silva", "Loyola","Carlino"])
        codigoDestino = mostarDestino(validar(random.randint(100,103), 100,103))
        codigoDeClase = validar(random.randint(1,10),1,10)
        monto = random.randint(5000,10000)
        vect.append(informacionDeVenta(pasaporte,name,codigoDestino,codigoDeClase,monto))
    printVect(vect)
def validar(num,a,b):
    bandera = True
    while bandera:
        if num >= a and num <= b:
            bandera = False
            return num
        else:
            num = int(input(f'dato erroneo, tiene que ser un numero entre {a} y {b}: '))
def max_to_min(vect):
    for i in range(len(vect)-1):
        for j in range(i+1,len(vect)):
            if int(vect[i].monto) < int(vect[j].monto):
                vect[i],vect[j]=vect[j],vect[i]
    return vect
def mostarDestino(num):
    tupla = 'Bahamas', 'Bermudas', 'Puerto Rico', 'República Dominicana'
    num = num %100
    return tupla[num]

def punto2(vect):
    vect = max_to_min(vect)
    printVect(vect)
def printVect(vect):
    for i in range(len(vect)):
        print(vect[i])
def generadorCaracteres(aleatorio):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(aleatorio))
def punto3(vect):
    vectPrint = vectContador(vect)
    bandera = True
    for i in range(len(vectPrint)):
        if vectPrint[i] != 0:
            print(f'La clase {i+1} recaudo {vectPrint[i]}')
        if bandera or may < vectPrint[i]:
            may = vectPrint[i]
            mayIndice = i+1
            bandera = False
    print(f'la clase {mayIndice} tuve el mayor recaudo con un total de {may}')

def vectContador(vect):
    vectContador = [0]*10
    for i in range(len(vect)):
        vectContador[vect[i].codeClase-1] += vect[i].monto
    return vectContador
def punto4(vect):
    vectorPromedio3 = vectContador(vect)
    sumaPromedio = j = 0
    for i in range(len(vect)):
        if vect[i].codeClase == 3 and vectorPromedio3[2]:
            sumaPromedio = vect[i].codeClase
            j +=1
    print(f'el promedio de la clase 3 fue de: {promedio(sumaPromedio,j)}')
def promedio(a,b):
    if b == 0:
        return "no hubo ventas en clases 3"
    else:
        return a//b
def punto5(vect,x):
    pos = None
    for i in range(len(vect)):
        if vect[i].pasaporte == x:
            pos = i
            break
    return pos