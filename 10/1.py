"""
1. Determinar la cantidad de todos los números que son negativos; también 
determinar la suma de números mayores o iguales a cero pero menores que 
600, y cuántos números son mayores o iguales que 200 pero además tienen el 
último dígito igual a 2 o igual a 3 (el resto de dividir por 10 debe ser 2 o 3). 
2. Determinar el promedio entero de todos los números generados que sean 
menores a cero pero que además sean divisibles por 4. Aclaración: NO se pide el 
promedio redondeado, sino el promedio truncado, sin decimales. 
"""

import random
random.seed(10)

cantNegativo = 0
sumNumberMenor600 = 0
cantMay200lastDigit23 = 0
cantDivisible4 = 0
sumDivisible4 = 0
impar = True
divisible2 = 0
for i in range(10000):
    number = random.randint(-500,1000)
    if number < 0:
        cantNegativo += 1
        if number % 4 == 0:
            sumDivisible4 += (number)
            cantDivisible4 += 1
        if number % 2 == 0:
            divisible2 += 1
    if number >= 0 and number < 600:
        sumNumberMenor600 += number
    lastDigit = number % 10
    #!TENER CUIDADO CON EL ULTIMO DIGITO
    if number >= 200 and (lastDigit == 2 or lastDigit== 3):
        cantMay200lastDigit23 += 1
    """
    3. Determinar el menor entre todos los números generados que sean impares y 
    mayores a 100. 
    """
    if number % 2 != 0 and number>100:
        if impar or menorimpar > number:
            menorimpar = number
            impar = False
    """
    4. Determinar el porcentaje entero que la cantidad de números negativos pares 
    representa sobre la cantidad total de números. Observación: en el cálculo de 
    este porcentaje, haga primero la multiplicación que corresponda, y luego la 
    división
    """
print("ultimo digito 2 y 3 y mayor que 200:", cantMay200lastDigit23)
print("menor que 600 mayor o igual que 0:",sumNumberMenor600)
print(sumDivisible4//cantDivisible4,"DE PROMEDIO")
print(str((divisible2*100)//10000)+"%")
print("el menor impar y mayor que 100:",menorimpar)
print(cantNegativo)