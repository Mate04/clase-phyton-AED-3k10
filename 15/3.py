import random
promedio = lambda sum,total: sum // total
n = random.randint(5,10)
vector = n * [0]
vectorMenor = []
vectorPrimo = []
contadorPunto1 = 0
for i in range(n):
    vector[i] = random.randint(1, 10)
for i in range(n):
    if vector[i] == vector[-1]:
        contadorPunto1 +=1
    if vector[0] > vector[i]:
        vectorMenor.append(vector[i])
    if vector[i] % 2 != 0:
        vectorPrimo.append(vector[i])
print(vector)
print(f'se repitio el ultimo numero de dicho vector {contadorPunto1-1}')
print(f'el vector menor formado aca es el siguiente {vectorMenor}')
print(f'el vector formado con numeros primos son {vectorPrimo}')
suma = 0
for i in range(len(vectorMenor)):
    suma +=vectorMenor[i]
print(promedio(suma,len(vectorMenor)))
