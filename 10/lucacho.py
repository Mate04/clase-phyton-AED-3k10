"""
Determinar cuántos eran mayores o iguales a 1 pero menores a 15000 y además eran divisibles por 4; cuántos eran mayores o iguales a 15000 pero menores que 22000 pero además eran pares, y cuántos eran mayores o iguales a 22000 pero además eran divisibles por 7.
Determinar la suma de todos los números generados que estén entre 4000 y 11000 (incluídos ambos).
Determinar el menor entre todos los números generados cuyos últimos dos dígitos sean iguales a 23 (es decir, aquellos cuyo resto al dividir por 100 es igual a 23).
Determinar el porcentaje entero que la cantidad de números entre 4000 y 11000 (incluidos ambos) representa sobre la cantidad total de números. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy presente en donde dejó ese archivo). Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas relacionados con él.
"""

#Autor Lucas Cuello 92765
import random
#Carga de datos
random.seed(47)
numerangue1_15000=0
numerangue2_22000=0
numerangue3_may22000=0
sumanum=0
suma=0
menornum=0
bandera=True
r=0
cantidad=0
bandera2=True
#Inicio del Ciclo
for k in range(13000) :
    num=random.randint(1,33000)  #carga de numeros
    cantidad +=1
    if num >= 1 and num <15000 and num % 4 == 0:   #punto numero 1.1
        numerangue1_15000 += 1
    if num >= 15000 and num <22000 and num % 2 == 0 :   #punto numero 1.2
        numerangue2_22000 += 1
    if num >= 22000 and num % 7 ==0:    #punto numero 1.3
        numerangue3_may22000 += 1
    if num >=4000 and num <=11000 : #punto numero 2
            sumanum += num
    if num % 100 == 23:   #punto numero 3
        if bandera == True :
            menornum = num
            bandera=False
    if menornum > num :
        numenor= num
    if num>= 4000 and num <= 11000 :  #punto numero 4 , este punto sigue en el ultimo print
        r+=1
#Fin
print("numeros mayores o iguales a 1 y menores a 15000 ,divisibles por 4: ", numerangue1_15000)
print("numeros mayores a 15000 y menores a 22000 ,pares : ",numerangue2_22000)
print("numeros mayores a 22000 divisibles por 7 : ",numerangue3_may22000)
print("suma de numeros entre 4000 y 11000 : ",sumanum)
print("el menor entre todos los numeros generados cuyos dos ultimos digitos son iguales a 23 :",menornum)
print("porcentaje entero de numeros entre 4000 y 11000 : ",((r * 100 )// cantidad))# segunda parte punto numero 4