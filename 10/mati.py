n = int(input("Ingrese un numero entero (con cero se termina): \n"))
mult6 = 0
antp = 0
ant = 0
new = 0
cont_divisor = 0
cont_ascendente_impares = 0
cont_maximo = 0
suma_multiplos6 = 0
while n != 0:
    antp,ant,new = ant,new,n
    if n % 6 == 0:
        suma_multiplos6 += n
        mult6 += 1
    if ant != 0:
        if ant % new == 0:
            cont_divisor += 1
    if (antp < ant < new) and (antp % 2 != 0 and ant % 2 != 0 and new % 2 != 0):
        cont_ascendente_impares += 1
        if cont_ascendente_impares == 1:
            cont_maximo += 1
    else: 
        cont_ascendente_impares = 0
    n = int(input("Ingrese otro numero: \n"))
if mult6 != 0:
    promedio = suma_multiplos6/mult6
    print("El promedio de los numeros multiplos de 6 es:", promedio)
print("La cantidad de numeros que son son divisores exactos del anterior es",cont_divisor)
print("Cantidad de veces que se genero una secuencia ascendente fue",cont_maximo)