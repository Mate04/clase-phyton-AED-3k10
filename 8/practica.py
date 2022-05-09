separador = "=" * 20 
numeroProcesar = int(input('Numero de vueltas: '))
contadorPositivo = 0
contadorNegativos = 0
SumaDePositivos = 0
if numeroProcesar > 1:
    bandera = True
    for i in range(numeroProcesar):
        print("\033[36m"+"vuelta "+str(i+1)+"/"+str(numeroProcesar))
        numero = int(input('Ingrese numero '))
        if i == 0:
            primerMenor = numero
        elif i == 1:
            segundoMenor = numero
            if segundoMenor < primerMenor:
                primerMenor, segundoMenor = segundoMenor, primerMenor
        elif i != 0 and i != 1:
            if numero < segundoMenor and numero > primerMenor:
                segundoMenor = numero
            elif numero < primerMenor:
                primerMenor, segundoMenor = numero, primerMenor
        if numero > 0:
            contadorPositivo += 1
            SumaDePositivos += numero
        if numero < 0:
            if contadorNegativos > 0:
                if mayNegative < numero:
                    mayNegative = numero
            else:
                mayNegative = numero
            contadorNegativos +=1
else:
    bandera = False
    print('No es posible poder procesar esa cantidad de numeros')
print('\033[33m'+separador)
if contadorPositivo > 0:
    print('los numeros positivos que se cargaron fueron:',contadorPositivo)
    promedio = SumaDePositivos/contadorPositivo
    print('El promedio de numeros positivos es', promedio)
    print(separador)
if contadorNegativos > 0:
    print('Los numeros negativos que se cargaron fueron', contadorNegativos)
    print('Y el mayor de los negativos fueron',mayNegative)
    print(separador)
if bandera:
    print('el segundo menor numero fue ', segundoMenor)
    print('el numero mas chico cargado fue', primerMenor)
    print(separador)