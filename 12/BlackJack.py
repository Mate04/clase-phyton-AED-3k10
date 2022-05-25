#inicio del programa
import random
#Para installar esta libreria, abra su terminal e escriba el siguiente comando: pip install pyfiglet
from pyfiglet import figlet_format

#colores
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
separador = '=' * 60
separadorPiola = MAGENTA+'<' * 30 + '>' * 30+BLANCO

#DATOS

palos = ("Treboles","Diamantes","Corazones","Picas")
valores = ["As",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
figuras = ["J", "Q", "K", "As"]

#Declaramos la variable pozo y cumplimos las condiciones
print(separadorPiola)
print(figlet_format('|| BlackJack ||', font='big'))
print(separadorPiola)
pozo = int(input('Cuanto dinero quiere destinar al pozo: \n'))

while pozo > 100000 or pozo < 0:
    print(ROJO+'El dinero que ingreso es mayor a 100000, por favor ingrese un valor menor')
    pozo = int(input('Cuanto dinero quiere destinar al pozo: \n'+BLANCO))
#declaramos funciones
def apostar(apuesta):   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS APUESTAS
    pozo -= apuesta
    return pozo

def menu():
    print(CYAN+separador)      #AQUI DEFINIMOS EL FUNCIONAMIENTO DEL MENU
    print('Opcion 1: Recargar dinero de pozo')
    print('Opcion 2: JUGAR UNA MANO')
    print('Opcion 3: SALIR')
    op = int(input('Elija una opcion (1/2/3): ')) 
    print(separador+BLANCO)
    return op

def cambiar_valor(carta):   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LOS VALORES DE AS
    if carta == "As":
            carta = 11
    elif carta in figuras:
            carta = 10
    valor_equivalente = carta
    return valor_equivalente

def generar_carta():   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS CARTAS DEL JUEGO
    palo = random.choice(palos)
    valor = random.choice(valores)
    carta = valor
    print(f'{valor} de {palo}')
    if (carta == "As") or (carta in figuras):
        carta = cambiar_valor(carta)
    return carta

def suma_cartas(a:int,b:int):     #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LA SU
    if (a + b) > 21 and b == 11:
        b = 1
    return a + b

op = menu()
while op != 3:
    if op == 1:
        pozo = int(input('Cuanto queres recargar al pozo?\n'))
    elif op == 2:
        print('Tus cartas son:')
        c1_jugador = generar_carta()
        c2_jugador = generar_carta()
        sumaJugador = suma_cartas(c1_jugador,c2_jugador)
        print("La suma de tus cartas es:",sumaJugador)
        print(separador)
        print("La carta del crupier es: ")
        c1_crupier = generar_carta()
        print(separador)
        seguir = input("Desea pedir otra carta (presione s=(si)/n=(no)): \n")
        while seguir != "n":
            carta_jugador = generar_carta()
            sumaJugador = suma_cartas(sumaJugador,carta_jugador)
            if sumaJugador < 21:
                print("La suma total de tus cartas es:",sumaJugador)
                print(separador)
                seguir = input("Desea pedir otra carta (presione s=(si)/n=(no)): \n")
            else:
                print(f"Te pasaste de 21 gil, tu suma es {sumaJugador}")
                print(separador)
                break
        print(input(ROJO+f'La suma parcial de tus cartas es {sumaJugador}')+BLANCO)       

    elif op != 1 and op != 2 and op != 3:
        print("Opcion invalida, porfavor elija una opcion validad")
        #si quiere continuar
        
    op = menu()