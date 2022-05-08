import random

#Bienvenida al programa
print("Bienvenido")
print("1. Jugar")
print("2. Salir")
opcion = int(input(("     Elegir opcion:")))
if opcion == 1:
    print("\nBienvenido a BlackJack")
    print("\nRonda 1:")
elif opcion == 2:
    print("Gracias por jugar")
    exit()
else:
    print("Opcion invalida")
    exit()

#Baraja de cartas
cartas_posibles = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
palos_posibles = ("Corazones", "Diamantes", "Treboles", "Picas")

suma_jugador = 0
suma_crupier = 0

#-------------------------------------------------------------------------
#Cartas del jugador, puede tener hasta 3 si se cumplen las condiciones
jugador_aleatoria_carta = random.randrange(0, 13), random.randrange(0, 13), random.randrange(0, 13)
jugador_palo_aleatorio = random.randrange(0, 4), random.randrange(0, 4), random.randrange(0, 4)

#Cartas del crupier
crupier_aleatoria_carta = random.randrange(0, 13), random.randrange(0, 13), random.randrange(0, 13)
crupier_palo_aleatorio = random.randrange(0, 4), random.randrange(0, 4), random.randrange(0, 4)
#--------------------------------------------------------------------------


#--------------------------------------------------------------------------
#Ver si tienen el mismo palo las primeras cartas
if palos_posibles[jugador_palo_aleatorio[0]] ==  palos_posibles[crupier_palo_aleatorio[0]]:
    print("Los primeros palos del jugador y el crupier son iguales.")

#ver si ademas de tener el mismo palo tienen la misma carta
    if cartas_posibles[jugador_aleatoria_carta[0]] == cartas_posibles[crupier_aleatoria_carta[0]]:
        print("Ademas los primeros numeros de los palos son iguales.")

#determina si aparecio una figura en el jugador y mostrar cartas que le tocaron
if (jugador_aleatoria_carta[0] == 0) or (jugador_aleatoria_carta[0] == 10) or (jugador_aleatoria_carta[0] == 11) or (jugador_aleatoria_carta[0] == 12):
    print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[0]], "de", palos_posibles[jugador_palo_aleatorio[0]])
    print("El jugador tiene la figura:", cartas_posibles[jugador_aleatoria_carta[0]])
    #sumar puntos por figura
    suma_jugador = suma_jugador + 11
#sumar puntos por tener numeros y mostrar cartas que le tocaron
else:
    print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[0]], "de", palos_posibles[jugador_palo_aleatorio[0]])
    suma_jugador = suma_jugador + cartas_posibles[jugador_aleatoria_carta[0]]

#determina si aparecio una figura en el crupier
if (crupier_aleatoria_carta[0] == 0) or (crupier_aleatoria_carta[0] == 10) or (crupier_aleatoria_carta[0] == 11) or (crupier_aleatoria_carta[0] == 12):
    print("Cartas del Crupier:", cartas_posibles[crupier_aleatoria_carta[0]], "de", palos_posibles[crupier_palo_aleatorio[0]])
    print("El crupier tiene la figura:", cartas_posibles[crupier_aleatoria_carta[0]])
    #sumar puntos por figura
    suma_crupier = suma_crupier + 11
else:
    #sumar puntos por tener numeros
    print("Cartas del Crupier:", cartas_posibles[crupier_aleatoria_carta[0]], "de", palos_posibles[crupier_palo_aleatorio[0]])
    suma_crupier = suma_crupier + cartas_posibles[crupier_aleatoria_carta[0]]

#mostrar suma
print("El jugador sumo:", suma_jugador, "puntos")
print("El crupier sumo:", suma_crupier, "puntos")
#--------------------------------------------------------------------------

print("\nRonda 2:")
#REPEEEEEEEEEEEEEEEEEETIRRRRRRRRRRRRRRRRRRRRRRRRRRRR

#---------------------------------------------------------------------------
#verificar si puede recibir otro AS el jugador
if (jugador_aleatoria_carta[1] == 0) or (jugador_aleatoria_carta[1] == 10) or (jugador_aleatoria_carta[1] == 11) or (jugador_aleatoria_carta[1] == 12):
    #mostrar que figura tiene el jugador
    print("El jugador tiene la figura:", cartas_posibles[jugador_aleatoria_carta[1]])

    #mostrar carta del jugador
    print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[1]], "de", palos_posibles[jugador_palo_aleatorio[1]])
    if (suma_jugador >= 11):
        print("                   El AS valdra como 1 punto")
        suma_jugador = suma_jugador + 1
    else:
        print("                   El AS valdra como 11 puntos")
        suma_jugador = suma_jugador + 11
#sumar puntos por una carta de numero
else:
    #mostrar carta del jugador
    print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[1]], "de", palos_posibles[jugador_palo_aleatorio[1]])
    #sumar
    suma_jugador = suma_jugador + cartas_posibles[jugador_aleatoria_carta[1]]


#verificar si puede recibir otro AS el crupier
if (crupier_aleatoria_carta[1] == 0) or (crupier_aleatoria_carta[1] == 10) or (crupier_aleatoria_carta[1] == 11) or (crupier_aleatoria_carta[1] == 12):
    #figura que tiene el crupier
    print("El crupier tiene la figura:", cartas_posibles[crupier_aleatoria_carta[1]])
    #mostrar carta del jugador
    print("Cartas del crupier:", cartas_posibles[crupier_aleatoria_carta[1]], "de", palos_posibles[crupier_palo_aleatorio[1]])
    if (suma_crupier >= 11):
        print("                   El AS valdra como 1 punto")
        suma_crupier = suma_crupier + 1
    else:
        print("                   El AS valdra como 11 puntos")
        suma_crupier = suma_crupier + 11
#sumar puntos por una carta de numero
else:
    #mostrar carta del jugador
    print("Cartas del crupier:", cartas_posibles[crupier_aleatoria_carta[1]], "de", palos_posibles[crupier_palo_aleatorio[1]])
    #sumar
    suma_crupier = suma_crupier + cartas_posibles[crupier_aleatoria_carta[1]]

#mostrar suma
print("El jugador sumo:", suma_jugador, "puntos")
print("El crupier sumo:", suma_crupier, "puntos")

#---------------------------------------------------------------------------
print("\nRonda 3:")
#---------------------------------------------------------------------------
#verificar si supera los 16 puntos
if (suma_jugador >= 17):
    print("El jugador no puede alzar más cartas")
else:
    #verificar si puede recibir otro AS el jugador
    if (jugador_aleatoria_carta[2] == 0) or (jugador_aleatoria_carta[2] == 10) or (jugador_aleatoria_carta[2] == 11) or (jugador_aleatoria_carta[2] == 12):
        #mostrar que figura tiene el jugador
        print("El jugador tiene la figura:", cartas_posibles[jugador_aleatoria_carta[2]])

        #mostrar carta del jugador
        print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[2]], "de", palos_posibles[jugador_palo_aleatorio[2]])
        if (suma_jugador >= 11):
            print("                   El AS valdra como 1 punto")
            suma_jugador = suma_jugador + 1
        else:
            print("                   El AS valdra como 11 puntos")
            suma_jugador = suma_jugador + 11
#sumar puntos por una carta de numero
    else:
        #mostrar carta del jugador
        print("Cartas del jugador:", cartas_posibles[jugador_aleatoria_carta[2]], "de", palos_posibles[jugador_palo_aleatorio[2]])
        #sumar
        suma_jugador = suma_jugador + cartas_posibles[jugador_aleatoria_carta[2]]

#verificar si no supera los 16 puntos
if (suma_crupier >= 17):
    print("El crupier no puede alzar más puntos")
else:
    #verificar si puede recibir otro AS el crupier
    if (crupier_aleatoria_carta[2] == 0) or (crupier_aleatoria_carta[2] == 10) or (crupier_aleatoria_carta[2] == 11) or (crupier_aleatoria_carta[2] == 12):
        #figura que tiene el crupier
        print("El crupier tiene la figura:", cartas_posibles[crupier_aleatoria_carta[2]])
        #mostrar carta del jugador
        print("Cartas del crupier:", cartas_posibles[crupier_aleatoria_carta[2]], "de", palos_posibles[crupier_palo_aleatorio[2]])
        if (suma_crupier >= 11):
            print("                   El AS valdra como 1 punto")
            suma_crupier = suma_crupier + 1
        else:
            print("                   El AS valdra como 11 puntos")
            suma_crupier = suma_crupier + 11
    #sumar puntos por una carta de numero
    else:
        #mostrar carta del jugador
        print("Cartas del crupier:", cartas_posibles[crupier_aleatoria_carta[2]], "de", palos_posibles[crupier_palo_aleatorio[2]])
        #sumar
        suma_crupier = suma_crupier + cartas_posibles[crupier_aleatoria_carta[2]]

#mostrar puntos
print("\nEl jugador sumo:", suma_jugador, "puntos")
print("El crupier sumo:", suma_crupier, "puntos")


#verificar si perdieron el crupier y el jugador por pasar el limite de puntos
if (suma_crupier > 21):
    print("\nEl crupier ha perdido, sobrepaso los limites de puntos")
    suma_crupier = 0
if (suma_jugador > 21):
    print("\nEl jugador ha perdido, sobrepaso los limites de puntos")
    suma_jugador = 0

#verificar quien tiene más puntos
if (suma_jugador > suma_crupier):
    print("El jugador ha ganado!")
elif (suma_jugador < suma_crupier):
    print("El crupier ha ganado!")
elif (suma_jugador == suma_crupier):
    print("El jugador y el crupier han empatado")