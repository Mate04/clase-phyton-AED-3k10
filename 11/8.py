option = int(input('\nopcion 1: Tabla de multiplicacion\nopcion 2: mayor y menor\noptions 3: ingresar por teclado dos valores a y b, siendo a positivo y b mayor que a (validarlo)\noption 4: texto\n'))
while option != 0:
    if option == 1:
        number = int(input('que numero queres ver de la tabla numerica?\n'))
        if number != 0:
            for i in range(1,11,1):
                print(str(i)+'x'+str(number)+': '+str((i)*number))
        else:
            print('no se puede porfavor ingresar un numero positivo mayor que 0')
    elif option == 2:
        numeroAprocesar = True
        banderaMenor = True
        banderaMay = True
        vueltaDada2do = 0
        while numeroAprocesar != 0:
            numeroAprocesar = int(input('que numero quieres ingresar a la base para procesar / finaliza la carga con 0\n'))
            if (banderaMenor or numeroAprocesar < menorProcesado) and numeroAprocesar != 0:
                menorProcesado = numeroAprocesar
                banderaMenor = False
            if (banderaMay or numeroAprocesar > mayorProcesado) and numeroAprocesar != 0:
                mayorProcesado = numeroAprocesar
                banderaMay = False
            vueltaDada2do += 1
        if vueltaDada2do > 1:
            print('el numero mayor procesado es',mayorProcesado)
            print('el numero menor procesado es',menorProcesado)
    elif option == 3:
        a = int(input('asignar valor a: '))
        b = int(input('asignar valor b: '))
        if a > 0 and b > a:
            suma = 0
            for i in range(a,b+1):
                if i % a == 0:
                    print(i)
                    suma += i
            print('la suma de los multiplos de',a,'hasta',b,'es',suma)
        else:
            print('el valor de A debe ser mayor que cero y el valor de B debe ser mayor que a')
    elif option == 4:
        texto = input('ingresar texto finalizando con un punto: \n')
        while texto[-1] != '.':
            texto = input('ingresar texto finalizando con un punto porfavor: \n')
        for letra in texto:
            if letra ==".":
                pass
            else:
                pass
    elif option == 0:
        print('salir')  
    else:
        print('opcion invalida, porfavor ingrese una opcion valida')
    option =int(input('quieres hacer otra operacion\nopcion 1: Tabla de multiplicacion\nopcion 2: mayor y menor\noptions 3: ingresar por teclado dos valores a y b, siendo a positivo y b mayor que a (validarlo)\noption 4: texto\n'))