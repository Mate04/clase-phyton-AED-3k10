#__authors__ = "David Ivan Becker", "Tomás Agustin Solazzi Constable", "Gonzalo Del Castillo", "Thiago Maldonado"
import random
#Bienvenida al programa
nombre = input("Ingrese su nombre: ")
print("Bienvenido", nombre)
print("Elija una opcion:")
print("1. Jugar")
print("2. Salir")
opcion = int(input())
if opcion == 1:
    print("\nBienvenido al BlackJack🎉")
elif opcion == 2:
    print("\nGracias por jugar🙌")
    exit()
else:
    print("\nOpcion invalida")
    exit()

#Baraja de cartas
possible_cards = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
palo_posible = ("Corazones", "Diamantes", "Treboles", "Picas")

jugador1 = random.choice(possible_cards)
jugador1_palo = random.choice(palo_posible)
jugador2 = random.choice(possible_cards)
jugador2_palo = random.choice(palo_posible)
crupier1 = random.choice(possible_cards)
crupier1_palo = random.choice(palo_posible)
crupier2 = random.choice(possible_cards)
crupier2_palo = random.choice(palo_posible)
#Print primeras y segundas cartas
print("\033[33m" + f"Cartas de {nombre} :", jugador1, "de", jugador1_palo, "y", jugador2, "de", jugador2_palo + "\033[0m")
print("\033[34m"+"\nLas cartas del crupier son:", crupier1, "de", crupier1_palo, "y", crupier2, "de", crupier2_palo + "\033[0m")

if jugador1 == crupier1 and jugador1_palo == crupier1_palo:
    print ("\033[32m" + "\nLas primeras cartas de ambos son iguales" + "\033[0m")
elif jugador1_palo == crupier1_palo:
    print("\033[32m" + "\nLas primeras cartas de ambos son del mismo palo" + "\033[0m")

#Cambio de la primera carta del jugador
if jugador1 == "A":
    jugador1 = 11
elif jugador1 == "J" or jugador1 == "Q" or jugador1 == "K":
    jugador1 = 10

#Cambio de la primera carta del crupier
if crupier1 == "A":
    crupier1 = 11
elif crupier1 == "J" or crupier1 == "Q" or crupier1 == "K":
    crupier1 = 10

#Cambio de la segunda carta del jugador
if jugador1 == 11 and jugador2 == "A":
    jugador2 = 1
elif jugador2 == "A":
    jugador2 = 11
elif jugador2 == "J" or jugador2 == "Q" or jugador2 == "K":
    jugador2 = 10
#Cambio de la segunda carta del crupier
if crupier1 == 11 and crupier2 == "A":
    crupier2 = 1
elif crupier2 == "A":
    crupier2 = 11
elif crupier2 == "J" or crupier2 == "Q" or crupier2 == "K":
    crupier2 = 10

#Suma de las cartas del jugador y Crupier
suma_player = jugador1 + jugador2
print("\033[33m" + f"\nLa suma de las cartas de {nombre} es:", suma_player, "\033[0m")
suma_crupier = crupier1 + crupier2
print("\033[34m""\nLa suma de las cartas del crupier es:", suma_crupier, "\033[0m")

#Verificacion de la suma de las cartas
if suma_player == 21 and suma_crupier == 21:
    print("\033[36m" + "\nHa sido un empate" + "\033[0m")
elif suma_player == 21 and suma_crupier != 21:
    print("\033[32m" + "\n¡¡Felicidades!! Ganaste" + "\033[0m")
elif suma_crupier == 21 and suma_player != 21:
    print("\033[31m" + "\n¡Oh no!! El crupier gano" + "\033[0m")
    
#Comprobando si jugador saca la tercera carta
if suma_player < 17:
    jugador3 = random.choice(possible_cards)
    jugador3_palo = random.choice(palo_posible)
    print("\033[33m" + "Tu tercera carta es:", jugador3, "de", jugador3_palo, "\033[0m")
    if jugador3 == "A" and suma_player > 10:
        jugador3 = 1
    elif jugador3 == "A":
        jugador3 = 11
    elif jugador3 == "J" or jugador3 == "Q" or jugador3 == "K":
        jugador3 = 10
#Suma de Jugador con la tercera carta
    suma_player = suma_player + jugador3
    print ("\033[33m" + "\nLa suma de tus cartas es", suma_player, "\033[0m")

#Comprobando si Crupier saca 3 carta    
if suma_crupier < 17:
    crupier3 = random.choice(possible_cards)
    crupier3_palo = random.choice(palo_posible)
    print("\033[34m" + "\nLa tercera carta del crupier es:", crupier3, "de", crupier3_palo, "\033[0m")
    if crupier3 == "A" and suma_crupier > 10:
        crupier3 = 1
    elif crupier3 == "A":
        crupier3 = 11
    elif crupier3 == "J" or crupier3 == "Q" or crupier3 == "K":
        crupier3 = 10
    #Suma del crupier con la tercera carta
    suma_crupier = suma_crupier + crupier3
    print ("\033[34m" + "\nEl total del crupier es:", suma_crupier, "\033[0m")

#Resultados finales
if suma_player > 21 and suma_crupier > 21:
    print("\033[36m" + "¡Oh no!! ambos se pasaron de 21, es un empate" + "\033[0m")
elif suma_player > 21 and suma_crupier <= 21:
    print("\033[31m" + "¡Oh no!! El crupier gano" + "\033[0m")
elif suma_crupier > 21 and suma_player <= 21:
    print("\033[32m" + f"¡Felicidades {nombre}!! Ganaste" + "\033[0m")
elif suma_player > suma_crupier:
    print("\033[32m" + f"¡Felicidades {nombre}!! Ganaste" + "\033[0m")
elif suma_crupier > suma_player:
    print("\033[31m" + "Noooo 😢😭, El crupier gano" + "\033[0m")
elif suma_player == suma_crupier:
    print("\033[36m" + "\nFelicidades(? Es un empate, ambos obtuvieron la misma puntuacion" + "\033[0m")