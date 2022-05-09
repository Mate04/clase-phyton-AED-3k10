separador = "="*20
#contamos las vueltas dadas
SumaDeNumeroTotales = 0
#declaramos la bandera Impar para tomar el mayor
banderaImpar = False
#declaramos las varibles para los divisibles para 3
cantDivisible3 = 0
sumaDivisible3 = 0
#declaramos la siguiente variable para podes ejecutar el while
sucecionDeNumeros = True
while sucecionDeNumeros != 0:
    sucecionDeNumeros = int(input('que numero quieres agregar a la lista de carga? / 0 para salir \n'))
    if sucecionDeNumeros != 0 and sucecionDeNumeros % 3 == 0:
        cantDivisible3+= 1
        sumaDivisible3+= sucecionDeNumeros
    if sucecionDeNumeros % 2 != 0:
        if banderaImpar == False:
            mayNumeroImpar = sucecionDeNumeros
            banderaImpar = True
        elif mayNumeroImpar < sucecionDeNumeros:
            mayNumeroImpar = sucecionDeNumeros
    SumaDeNumeroTotales += sucecionDeNumeros

print(separador)
#sacar el porcentaje de numeros divisibles por 3
porcentajeDivisible3:float = (sumaDivisible3/SumaDeNumeroTotales)*100
print('el porcentaje de numeros que son divisibles por 3 es: {:.2f}'.format(porcentajeDivisible3))