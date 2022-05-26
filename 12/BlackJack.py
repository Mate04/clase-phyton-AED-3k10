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
separador_ganador_jugador = VERDE+"*"*60+BLANCO
separador_ganador_croupier = ROJO+"*"*60+BLANCO
separador_empate = AZUL+"*"*60+BLANCO

#DATOS
bandera=True
winNatural=0
winCrupier=0
winjugador=0
palos = ("Treboles","Diamantes","Corazones","Picas")
valores = ["As",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
figuras = ["J", "Q", "K"]

print(separadorPiola)
print(figlet_format('|| BlackJack ||', font='big'))
print(separadorPiola)
#Declaramos la variable pozo y cumplimos las condiciones
pozo = int(input('\nCuanto dinero quiere destinar al pozo: '))
while pozo > 100000 or pozo < 1:
    print(ROJO+'El dinero que ingreso debe ser menor a 100000 y mayor a 1 porfavor ingrese una cantidad valida')
    pozo = int(input(BLANCO+'Cuanto dinero quiere destinar al pozo: \n'+BLANCO))
#declaramos funciones
def apostar(apuesta:int):   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS APUESTAS
    while apuesta > pozo or apuesta < 1:
        print(ROJO+'No puede apostar esa cantidad, el pozo actual es de: '+str(pozo))
        apuesta = int(input(BLANCO+'Cuanto dinero quiere apostar: '))
    return apuesta

def menu():
    print("\n"+CYAN+separador+"\n")      #AQUI DEFINIMOS EL FUNCIONAMIENTO DEL MENU
    print ("-"*(30-9), "Menu de Opciones", "-"*(30-9), "\n")
    print(f"\nTu dinero actual del pozo es de {pozo}\n")
    print('Opcion 1: APOSTAR \nOpcion 2: JUGAR UNA MANO \nOpcion 3: SALIR')
    op = int(input('Elija una opcion (1/2/3): ')) 
    print("\n"+separador+BLANCO+"\n")
    return op

def cambiar_valor(carta):   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LOS VALORES DE AS
    if carta == "As":
            carta = 11
    elif carta in figuras:
            carta = 10
    return carta

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

op = True
while op != 3:
    if bandera or mayPozo < pozo:
        mayPozo = pozo
        bandera = False
    op = menu()
    if op == 1:
        recargaAlPozo = int(input('\nCuanto dinero quiere recargar: '))
        while recargaAlPozo > 100000 or recargaAlPozo < 1:
            print(ROJO+'\nEl dinero que pusiste es negativo o mayor a 100000, por favor ingrese un valor menor\n')
            recargaAlPozo = int(input(BLANCO+'Cuanto dinero quiere recargar?: '))
        pozo += recargaAlPozo
    elif op == 2:
        print("-"*10+" Juego "+"-"*10)
        apuesta = apostar(int(input('\nCuanto dinero quiere apostar: ')))
        print(input("\nPresione Enter para Comenzar..."))
        print('Tus cartas son:\n')
        c1_jugador = generar_carta()
        c2_jugador = generar_carta()
        sumaJugador = suma_cartas(c1_jugador,c2_jugador)
        #Suma Jugador
        print(f"\nLa Suma de tus Cartas es: {sumaJugador} \n")
        print(separador+"\n")
        #Parte Croupier
        print("La Primera Carta del Crupier es:\n")
        c1_crupier = generar_carta()
        suma_Crupier = c1_crupier
        #Pregunta para seguir generando cartas Jugador
        #contador de cartas
        banderaNatural = True
        co_cjugador= 2
        co_ccrupier= 1
        print("\n"+separador+"\n")
        seguir = input(f"Desea pedir otra carta? (Presione s = (si)/ n = (no) ): ")
        #Ciclo donde se genera una nueva carta al jugador
        while seguir != "n":
            carta_jugador = generar_carta()
            sumaJugador = suma_cartas(sumaJugador,carta_jugador)
            co_cjugador += 1
            if sumaJugador == 21:
                print("Sacaste 21\n")
                break
            elif sumaJugador < 21:
                print(f"La suma total de tus cartas es: {sumaJugador}\n")
                seguir = input("Desea pedir otra carta (presione s=(si)/n=(no)): ")
            else:
                print(f"Te pasaste de 21 gil, tu suma es {sumaJugador}\n")
                break
        print(separador+"\n")
        #parte del crupier para ver si toma o no cartas
        while suma_Crupier <= 16:
            print("El Croupier Pidio otra Carta\n")
            carta_crupier_generica = generar_carta()
            suma_Crupier = suma_cartas(suma_Crupier,carta_crupier_generica)
            co_ccrupier += 1
            
        
        
        print(f"\nEl crupier se planta con {suma_Crupier} puntos\n")
        
        #Condiciones De ganadores
        #Cuando Gana
        if sumaJugador > suma_Crupier and sumaJugador <= 21:
            pozo += apuesta
            winjugador += 1
            print(separador_ganador_jugador)
            print(VERDE+f"Has ganado ahora se te sumaran {apuesta} tu pozo actual es de: {pozo}"+BLANCO)
            print(separador_ganador_jugador)    
        #Cuando Empatan
        elif sumaJugador == suma_Crupier and sumaJugador <= 21:
            if sumaJugador == 21:
                if co_cjugador == 2 and co_ccrupier == 2:
                #EMPATAMOS
                    print(separador)
                    print("Ambos empatan al tener BlackJack Ntural")
                    print(separador)
                    banderaNatural = False
                elif co_cjugador == 2 and co_ccrupier != 2 :
                    #GANAMOS BlackJack
                    print(separador_ganador_jugador) 
                    print(VERDE+"Has Ganado Al tener BlackJack Natural contra el Croupier")
                    print(separador_ganador_jugador)
                    winjugador += 1
                    banderaNatural = False
                    winNatural += 1
                elif co_cjugador != 2 and co_ccrupier == 2:
                    winCrupier += 1
                    winNatural += 1
                    banderaNatural = False
                #PERDIMOS
                    print(separador_ganador_croupier)
                    print(ROJO+"Has Perdido contra el Croupier obtuvo BlackJack Natural")
                    print(separador_ganador_croupier)
            else:
            #EMPATAMOS
                print(separador_empate)
                print("Empate")
                print(separador_empate)
            #print(f"Empataron los dos tuvieron un puntaje de {suma_Crupier}\n")
            #Cuando Pierde
        #Gana Croupier    
        elif sumaJugador < suma_Crupier and suma_Crupier <= 21:
            pozo -= apuesta
            winCrupier += 1
            print(separador_ganador_croupier)
            print(ROJO+f"Has perdido contra el Croupier, se te restaran {apuesta} tu pozo actual va a ser {pozo}\n")
            print(separador_ganador_croupier)
        #Ambos se pasaron de 21  
        else:
            print(separador_ganador_croupier)
            print(ROJO+f"Has perdido contra el Croupier, se te restaran {apuesta} tu pozo actual va a ser {pozo}\n")
            print(separador_ganador_croupier)
            winCrupier += 1
        if co_ccrupier ==2 and suma_Crupier == 21 and banderaNatural:
            print(ROJO+"El Croupier tiene BlackJack Natural")
            winNatural += 1
        elif co_ccrupier == 2 and sumaJugador == 21 and banderaNatural:
            print(VERDE+"El jugador hizo un BlackJack Natural")
            winNatural += 1
        print(separador+BLANCO)
    elif op != 1 and op != 2 and op != 3:
        print("Opcion invalida, porfavor elija una opcion validad")
    
        #si quiere continuar
        
    
print(f'cantidad de veces que gano el crupier {winCrupier}')
print('cantidad de veces que gano el jugador',winjugador)
print('cantidad de veces que se gano una mano por blackjack natural',winNatural)
print('el valor maximo que alcanzo el pozo fue :',mayPozo)

