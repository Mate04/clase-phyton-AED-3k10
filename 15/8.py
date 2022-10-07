import random
class encuesta:
    def __init__(self,numeroCalza:int,color:str,edad:int,tipo:str):
        self.numeroCalza = numeroCalza
        self.color = color
        self.edad = edad
        self.tipo = tipo
    def getDetails(self):
        return [self.numeroCalza,self.color,self.edad,self.tipo]
encuestas = []
tiposCalzado = [0,0,0,0,0]
#punto 1
promedio=blanco=negro=azul=tela=cuero=0
for i in range(100):
    numeroCalza = random.randint(30,45)
    color = random.choice(["blanco","negro","azul"])
    edad = random.randint(10,15)
    tipo = random.choice(["cuero","tela"])
    encuestas.append(encuesta(numeroCalza,color,edad,tipo).getDetails())
for i in range(len(encuestas)):
    promedio += encuestas[i][0]
    #punto 2
    if 10 < encuestas[i][2] < 18:
        if encuestas[i][1] == 'blanco':
            blanco += 1
        elif encuestas[i][1] == 'negro':
            negro += 1
        else:
            azul += 1
    #punto 3
    if 19 < encuestas[i][2] < 25:
        if encuestas[i][4] == 'tela':
            tela += 1
        else:
            cuero += 1
    #punto 4
    #Si el numero de calzado va desde 35 a 40, generar un vector que contenga cual es la demanda de cada número de calzado (un vector contador de 6 elementos) y determinar cuál es el número de mayor y menor demanda.
    if 35 < encuestas[i][0] < 40:
        if encuestas[i][0] == 35:
            tiposCalzado[0] += 1
        elif encuestas[i][0] == 36:
            tiposCalzado[1] += 1
        elif encuestas[i][0] == 37:
            tiposCalzado[2] += 1
        elif encuestas[i][0] == 38:
            tiposCalzado[3] += 1
        elif encuestas[i][0] == 39:
            tiposCalzado[4] += 1
        else:
            tiposCalzado[5] += 1
#punto 2
if blanco > negro and blanco > azul:
    print('los jovenes entre 10 y 18 prefieren el blanco')
elif negro > blanco and negro > azul:
    print('los jovenes entre 10 y 18 prefieren el negro')
elif azul > blanco and azul > negro:
    print('los jovenes entre 10 y 18 prefieren el azul')
elif blanco == negro:
    print('los jovenes entre 10 y 18 prefieren el blanco y el negro')
elif blanco == azul:
    print('los jovenes entre 10 y 18 prefieren el blanco y el azul')
elif azul == negro:
    print('los jovenes entre 10 y 18 prefieren el negro y el azul')
#TODO: punto 3:
if cuero > tela:
    print('los jovenes 19 y 25 prefiero el cuero')
elif tela> cuero:
    print('los jovenes 19 y 25 prefiero la tela')
else:
    print('los jovenes 19 y 25 prefieren ambas')
#TODO: punto 5:
#buscar mayor sin usar la funcion max
mayor = 0
for i in range(len(tiposCalzado)):
    if tiposCalzado[i] > mayor:
        mayor = tiposCalzado[i]
        indice = i
print('el numero de calzado que mas se repite es: ',indice+35)
print(f'el promedio es de: {promedio//len(encuestas)}')