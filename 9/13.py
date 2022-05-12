vueltaYaDada = False
option = True
while option != 0:
    if vueltaYaDada:
        print('='*20)
    option = int(input("Opcion 1, opcion 2, opcion 3:, 0 para salir\n" ))
    if option == 1:
        banderaAnterior = False
        sumSiguiente = 0
        contadorNumero1 = 0
        secuenciaProcesar = int(input('Cuantos numeros queres procesar\n'))
        for i in range(secuenciaProcesar):
            number = int(input('numero que queres agregar\n'))
            if banderaAnterior and number != 1:
                sumSiguiente += number
                banderaAnterior = False
            if number == 1:
                banderaAnterior = True
                contadorNumero1 +=1
        if contadorNumero1 == secuenciaProcesar:
            print('usted es un pelotudo que solo puso 1 boludoooooo')
        else:
            print('la suma de los numeros despues de 1 es de:',sumSiguiente)
    if option == 2:
        secuenciaProcesar = False
        contarPrimerNumberVecesQPasa = 0
        contDeVecesQnoSeRepitioElPrimerNumero = 0
        i = 0
        #for i in range(secuenciaProcesar):
        while secuenciaProcesar != True:
            number = int(input('numero que queres agregar\n'))
            if i == 0:
                primerNumber = number
                contarPrimerNumberVecesQPasa += 1
            elif primerNumber == number and i != 0:
                contarPrimerNumberVecesQPasa += 1
                contDeVecesQnoSeRepitioElPrimerNumero = 0
            if primerNumber != number:
                contDeVecesQnoSeRepitioElPrimerNumero += 1
            if contDeVecesQnoSeRepitioElPrimerNumero == 5:
                secuenciaProcesar = True
            i += 1
        print('las cantidad de veces q hubo el primer numero fueron:',contarPrimerNumberVecesQPasa)
    if option == 3:
        number = True
        flags = False
        contNumberMenores = 0
        while number != 0:
            number = int(input("Numero que quieres agregar a la secuencia / finalizar con 0\n"))
            if flags and number != 0:
                if numberAnterior > number:
                    contNumberMenores += 1
            flags = True
            numberAnterior = number
        print('las veces q se contaron numeros menores a su antecesor es de:',contNumberMenores)
    if option != 1 and option != 2 and option != 3:
        print('usted elegio una opcion incorrecta vuelva a elegir\n')
    vueltaYaDada = True