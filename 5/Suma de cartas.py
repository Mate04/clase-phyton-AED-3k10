__author__ = "Mateo Maldonado 98717, Lucas Cuello Arrigoni 92765, Matias Sciarra 95034"
#Declaramos los colores de la consola
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

import random

print(CYAN + "Bienvenido al BlackJack")
#INGRESO DEL NOMBRE DEL JUGADOR
nombre = input(RED +"Ingrese su nombre: \n")
#PALOS DE LAS CARTAS
palos = ("Treboles", "Corazones", "Diamantes", "Picas")
valores = ("As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
separador= '_' *60
#COMIENZO DEL JUEGO
comienzo = int(input(CYAN+"Hola " + nombre + ", desea comenzar? \n 1-Si \n 2-No\n"))
if comienzo == 1:
    #declaramos un booleano para saber si toco un palo
    bandera = False
    #TODO: SEPARADOR
    print(BLUE ,separador)
    #parte del crupier
    carta1Crupier = [random.choice(valores), random.choice(palos)]
    carta2Crupier = [random.choice(valores), random.choice(palos)]
    #imprimimos valor de la carta del crupier
    print(BLUE + "La carta 1ra del crupier es: " + str(carta1Crupier[0]) + " de " + str(carta1Crupier[1]))
    print(BLUE + "La carta 2da del crupier es: " + str(carta2Crupier[0]) + " de " + str(carta2Crupier[1]))
    #Sumar Puntuacion
    if carta1Crupier[0] == "K" or carta1Crupier[0] == "Q" or carta1Crupier[0] == "J":
        bandera = True
        carta1Crupier[0] = 10
    if carta2Crupier[0] == "K" or carta2Crupier[0] == "Q" or carta2Crupier[0] == "J":
        bandera = True
        carta2Crupier[0] = 10
    #Si toca dos As vale 1 Sino 11
    if carta1Crupier[0] == "As" and carta2Crupier[0] == "As":
        carta1Crupier[0] = 11
        carta2Crupier[0] = 1
    elif carta1Crupier[0] == "As":
        carta1Crupier[0] = 11
    elif carta2Crupier[0] == "As":
        carta2Crupier[0] = 11
    #Esta es la suma de las 2 primeras cartas del Crupier
    sumaCrupier = carta1Crupier[0]+ carta2Crupier[0] 
    print(BLUE + "La suma de las cartas del crupier es:", sumaCrupier)
    #TODO: SEPARADOR nuevo apartado
    print(separador)
    #parte del jugador
    carta1Jugador = [random.choice(valores), random.choice(palos)]
    carta2Jugador = [random.choice(valores), random.choice(palos)]
    #imprimimos valor de la carta del jugador
    print(YELLOW,separador)
    print("La 1ra carta del jugador es: " + str(carta1Jugador[0]) + " de " + str(carta1Jugador[1]))
    print("La 2da carta del jugador es: " + str(carta2Jugador[0]) + " de " + str(carta2Jugador[1]))
    #Sumar Puntuacion
    if carta1Jugador[0] == "K" or carta1Jugador[0] == "Q" or carta1Jugador[0] == "J":
        bandera = True
        carta1Jugador[0] = 10
    if carta2Jugador[0] == "K" or carta2Jugador[0] == "Q" or carta2Jugador[0] == "J":
        bandera = True
        carta2Jugador[0] = 10
    #Si toca dos As vale 1 Sino 11
    if carta1Jugador[0] == "As" and carta2Jugador[0] == "As":
        carta1Jugador[0] = 11
        carta2Jugador[0] = 1
    elif carta1Jugador[0] == "As":
        carta1Jugador[0] = 11
    elif carta2Jugador[0] == "As":
        carta2Jugador[0] = 11
    #Esta es la suma de las 2 primeras cartas del Jugador
    sumaJugador = carta1Jugador[0]+ carta2Jugador[0]
    print("La suma de las cartas del jugador es:", sumaJugador)
    print(separador)
    
    #TODO: SEPARADOR
    print(BLUE ,separador)
    #parte del crupier
    if sumaCrupier == 21:
        print("El Crupier tiene BlackJack teniendo un", sumaCrupier)
    elif sumaCrupier > 21:
        print("El Crupier se paso teniendo un total de", sumaCrupier)
    else:
        if sumaCrupier <= 17:
            print("El Crupier tiene menos de 17 acumulando teniendo hasta el momento", sumaCrupier)
            carta3Crupier = [random.choice(valores), random.choice(palos)]
            print("La 3ra carta del crupier es: " + str(carta3Crupier[0]) + " de " + str(carta3Crupier[1]))
            if carta3Crupier[0] == "K" or carta3Crupier[0] == "Q" or carta3Crupier[0] == "J":
                bandera = True
                carta3Crupier[0] = 10
            if carta3Crupier[0] == "As" and sumaCrupier < 11:
                carta3Crupier[0] = 11
            elif carta3Crupier[0] == "As" and sumaCrupier > 11:
                carta3Crupier[0] = 1
            sumaCrupier = sumaCrupier + carta3Crupier[0]
            print("La suma total de las cartas del crupier es:", sumaCrupier)
        else:
            print("El Crupier no alza tercera carta teniendo un total de", sumaCrupier)
    print(separador)
    #TODO: SEPARADOR
    print(YELLOW ,separador)
    #parte del jugador
    if sumaJugador == 21:
        print("El Jugador tiene BlackJack teniendo un", sumaJugador)
    elif sumaJugador > 21:
        print("El Jugador se paso teniendo un total de", sumaJugador)
    else:
        if sumaJugador <= 17:
            print("El Jugador tiene menos de 17 acumulando teniendo hasta el momento", sumaJugador)
            carta3Jugador = [random.choice(valores), random.choice(palos)]
            print("La 3ra carta del jugador es: " + str(carta3Jugador[0]) + " de " + str(carta3Jugador[1]))
            if carta3Jugador[0] == "K" or carta3Jugador[0] == "Q" or carta3Jugador[0] == "J":
                bandera = True
                carta3Jugador[0] = 10
            if carta3Jugador[0] == "As" and sumaJugador < 11:
                carta3Jugador[0] = 11
            elif carta3Jugador[0] == "As" and sumaJugador > 11:
                carta3Jugador[0] = 1
            sumaJugador = sumaJugador + carta3Jugador[0]
            print("La suma total de las cartas del jugador es:", sumaJugador)
        else:
            print("El Jugador no alza tercera carta teniendo un total de", sumaJugador)
    print(separador)
    #TODO: SEPARADOR
    print(CYAN ,separador)
    #Comprobamos quien gana
    if sumaCrupier <= 21 and sumaJugador <= 21:
        if sumaCrupier > sumaJugador:
            print(RED,"El Crupier gana con un total de", sumaCrupier, "😔😔")
        elif sumaCrupier < sumaJugador:
            print(GREEN,"El Jugador gana con un total de", sumaJugador, "😄😄")
        else:
            print("Empate")
    elif sumaCrupier > 21 and sumaJugador <= 21:
        print(GREEN,"El Jugador gana con un total de", sumaJugador, "😄😄")
    elif sumaCrupier <= 21 and sumaJugador > 21:
        print(RED,"El Crupier gana con un total de", sumaCrupier, "😔😔")
    else:
        print(RED,"Pierden los dos", "😕")
    print(CYAN, separador)
else:
    print(RED, "Opcion no valida, se cancelo el juego 👻")
if carta1Crupier[0] == carta1Jugador[0] and carta1Crupier[1] == carta1Jugador[1]:
    print("Las cartas del crupier y del jugador son iguales tanto el palo como el valor\n ")
elif carta1Crupier[0] == carta1Jugador[0]:
    print("Las cartas del crupier y del jugador son iguales en el valor pero no en el palo\n ")
elif carta1Crupier[1] == carta1Jugador[1]:
    print("Las cartas del crupier y del jugador son iguales en el palo pero no en el valor\n ")
if bandera:
    print("En la partida hubo al menos un comodin")
print(separador)
