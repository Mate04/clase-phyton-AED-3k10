"""
Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios, usando como semilla del generador el número 20220512 (es decir random.seed(20220512)). Los valores de cada uno de esos 25000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números). A partir de esa sucesión el programa debe:

Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza con 1.
TODO:Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
Indicar el porcentaje entero que representa cada contador del punto 1. Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.
"""

import random
random.seed(20220512)

multiplo5but3dont = 0
multiplo3 = 0
dontMulti5and3 = 0
multi11 = 0

for i in range(25000):
    aleatorio = random.randint(1,45000)
    if aleatorio % 3 == 0:
        multiplo3 += 1
    if aleatorio % 5 == 0 and aleatorio % 3 != 0:
        multiplo5but3dont += 1
    if aleatorio % 5 != 0 and aleatorio % 3 != 0:
        dontMulti5and3 += 1
    if aleatorio % 2 == 0 and aleatorio % 11 == 0:
        multi11 +=1
total = multiplo3 + multiplo5but3dont + dontMulti5and3
print(multiplo3)
print(multiplo5but3dont)
print(dontMulti5and3)
print(str((total*100)//25000)+"%")
print("multi11", multi11)
