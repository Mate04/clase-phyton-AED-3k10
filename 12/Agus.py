#inicio del programa
import random
from tkinter import N

separador = '=' * 60 
separador1 = str("<"*30)+str(">"*30)
enter = ("Presione Enter para continuar... ")

#colores
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'

#DATOS

billetera = int(input('Cuanto dinero tiene para apostar?: \n'))
palos = ("Treboles", "Diamantes", "Corazones", "Picas")
valores = ["As", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
figuras = ["J", "Q", "K", "As"]
dinerodisponible = billetera
op = True

#declaramos funciones


def apostar():  #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS APUESTAS
    pozo = 0
    dinero_disponible = billetera
    nro_apostar = int(
        input(
            f'Cuanto dinero va a apostar?\nSu dinero disponible es {dinero_disponible}\n'
        ))
    pozo += nro_apostar
    return pozo


def menu():  #AQUI DEFINIMOS EL FUNCIONAMIENTO DEL MENU
    print("\n",separador1,"\n")
    print ("-"*10, "Menu de Opciones", "-"*10, "\n")
    print('Opcion 1: APOSTAR \nOpcion 2: JUGAR UNA MANO \nOpcion 3: SALIR')
    op = int(input('\nElija una opcion (1/2/3): '))
    print("\n",separador1,"\n")
    return op


def cambiar_valor(
        carta: list):  #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LOS VALORES DE AS
    if carta == "As":
        carta = 11
    elif carta in figuras:
        carta = 10
    valor_equivalente = carta
    return valor_equivalente


def generar_carta():  #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS CARTAS DEL JUEGO
    palo = random.choice(palos)
    valor = random.choice(valores)
    carta = valor
    print(f'{valor} de {palo}')
    if (carta == "As") or (carta in figuras):
        carta = cambiar_valor(carta)
    return carta


def suma_cartas(a: int, b: int):  #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LA SU
    if (a + b) > 21 and b == 11:
        b = 1
    suma = a + b
    return suma


op = menu()
while op != 3:
    if op == 1:
        dinerodisponible = dinerodisponible - apostar()
        print('Su dinero disponible es', dinerodisponible)
        menu()
    elif op == 2:
        print('Tus cartas son:\n')
        c1_jugador = generar_carta()
        c2_jugador = generar_carta()
        sumaJugador = suma_cartas(c1_jugador, c2_jugador)
        print("\nLa suma de tus cartas es:", sumaJugador, "\n")
        print(input(enter), "\n", separador,"\n")
        print("La carta del crupier es:\n")
        c1_crupier = generar_carta()
        print(input(enter), "\n", separador,"\n")
        seguir = input("Desea pedir otra carta (presione Y=(si)/N=(no)): ")
        while seguir == "Y" and sumaJugador < 21:
            carta_jugador = generar_carta()
            sumaJugador = suma_cartas(sumaJugador, carta_jugador)
            if sumaJugador < 21:
                print("\nLa suma total de tus cartas es:", sumaJugador)
                print(separador)
                seguir = input(
                    "\nDesea pedir otra carta (presione s=(si)/n=(no)): ")
            else:
                print("\n"f"Te pasaste de 21 gil, tu suma es {sumaJugador}")
                print(separador)
                break
        #si quiere continuar
        op = menu()
