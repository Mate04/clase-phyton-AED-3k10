from modulos import *

def main():
    bingo= False
    terminar = True
    numeroSalidos = [None]
    nombreJugador = input('como se llama: ')
    cartones = verificar(int(input('cuantos cargones quiere tener: ')),1,5)
    posicionNumeroTachado = [[]for i in range(cartones)]
    recompensa = 0
    barajasJugador = generadorDeBarajas(cartones, [],bandera=True,color='red')
    barajaMaquina = generadorDeBarajas(10-cartones, [],bandera=True,color='blue')
    while terminar != False:
        numeroSalido = random.randint(1,99)
        while numeroSalido in numeroSalidos:
            numeroSalido = random.randint(1,99)
        numeroSalidos.append(numeroSalido)
        print('\033[37m'+f'numero salido: {numeroSalido}')
        opcion = menu()
        while opcion != 0:
            if opcion == 1:
                numBaraja = verificar(int(input('En q numero de barja deseas tachar ')),1,len(posicionNumeroTachado))
                numero_tachar = int(input('que numero deseas tachar? '))
                tacharNumero(posicionNumeroTachado,numBaraja-1,numero_tachar)
            elif opcion == 2:
                printBarajas(barajasJugador,color='red')
            elif opcion == 3:
                numBaraja = verificar(int(input('que baraja decides ver?')),1,len(barajasJugador))
                printBaraja(barajasJugador[numBaraja-1],color='red')
            elif opcion == 4:
                for i in range(len(posicionNumeroTachado)):
                    print(f'numero de baraja tachado {i} = {posicionNumeroTachado[i]}')
            elif opcion == 5:
                numBaraja = verificar(int(input('en que baraja esta su linea: ')),1,len(barajasJugador))
                tipo = verificar(int(input('que tipo es fila(1) o columna(2), presione el numero: ')),1,2)
                if tipo == 1:
                    fila = verificar(int(input('en que fila se encuentra: ')),1,len(barajasJugador[1]))
                    bandera = verificarLinea(barajasJugador[numBaraja-1][fila-1],numeroSalidos)
                else:
                    matrizTransversal = matrizTransVersal(barajasJugador[numBaraja-1])
                    columna = verificar(int(input('en que columna se encuentra: ')),1,len(matrizTransversal))
                    bandera = verificarLinea(matrizTransversal[columna-1],numeroSalidos)
                if bandera:
                    recompensa += 5000
                else:
                    recompensa += 0
            opcion = menu()
            if opcion == 6:
                bingo = True
                print('Usted hizo bingo!!!')
                numBaraja = verificar(int(input('en que baraja esta su linea: ')),1,len(barajasJugador))
                for i in range(len(barajasJugador[numBaraja-1])):
                    bandera = verificarLinea(barajasJugador[numBaraja-1][i],numeroSalidos)
                    if not bandera:
                        bingo = False
                terminar = 0
                opcion = 0
            
        for i in range(len(barajaMaquina)):
            filas = 0
            for j in range(len(barajaMaquina[i])):
                bandera = verificarLinea(barajaMaquina[i][j],numeroSalidos)
                if bandera:
                    filas+=1
            if filas == 3:
                terminar = 0
                break

    if bingo:
        print('Usted hizo bingo')
    elif filas == 3:
        print('la maquina gano')
    else:
        print('Usted no hizo bingo')
            

main()

