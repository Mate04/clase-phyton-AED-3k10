#inicio del programa
import random

separador1 = '_' * 60
separador2 = '=' * 60
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

palos = ("Treboles","Diamantes","Corazones","Picas")
valores = ["As",2,3,4,5,6,7,8,9,10,"J","Q","K"]
figuras = ["J", "Q", "K", "As"]
op = True
#declaramos funciones
def menu():
    print('Opcion 1: APOSTAR')
    print('Opcion 2: JUGAR UNA MANO')
    print('Opcion 3: SALIR')
    op = int(input('Elija una opcion (1/2/3): \n'))  
    return op

def cambiar_valor(carta:list):
    if carta in figuras:
        if carta == "As":
            carta = 11
        else:
            carta = 10
    valor_equivalente = carta
    return valor_equivalente

def generar_carta():
    palo = random.choice(palos)
    valor = random.choice(valores)
    carta = valor
    print(f'{valor} de {palo}')
    if carta in figuras:
        valor = cambiar_valor(carta)
    return carta

def suma_cartas(a:int,b:int):
    suma = a + b
    return suma


op = menu()
while op != 3:
    if op == 1:
        pass
    elif op == 2:
        print('Tus cartas son:')
        c1_jugador = generar_carta()
        c2_jugador = generar_carta()
        sumaJugador = suma_cartas(c1_jugador,c2_jugador)
        print("La suma de tus cartas es:",sumaJugador)
        print("La carta del crupier es: ")
        c1_crupier = generar_carta()
        print(input("Enter para continuar..."))        
    op = menu()

#ejecucion

##player = input('Ingrese su nombre')
##pozo=int(input('De Cuanto dinero tiene para el pozo (NO MAYOR A 100.000):\n'))

