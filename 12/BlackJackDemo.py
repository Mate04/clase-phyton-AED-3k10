#inicio del programa
import random
import os
#TODO:Para installar esta libreria, abra su terminal e escriba el siguiente comando: pip install pyfiglet
from pyfiglet import figlet_format
def main():
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
    separadorNormal = '-' * 60

    #DATOS
    bandera=True
    winNatural=0
    winCrupier=0
    winjugador=0

    #vueltas dadas
    vueltasDados = 0    

    #declaramos varibales para la partida seguida
    seguidos = False
    seguidillaContador = 0
    banderaSeguidilla = True

    palos = ("Treboles","Diamantes","Corazones","Picas")
    valores = ["As",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    figuras = ["J", "Q", "K"]
    print(separadorPiola)
    print(figlet_format('|| BlackJack ||', font='big'))
    print(separadorPiola)
    jugador=input('ingrese su nombre:')
    #Declaramos la variable pozo y cumplimos las condiciones
    pozo = int(input('\nCuanto dinero quiere destinar al pozo:\t'))
    while pozo > 100000 or pozo < 1:
        print(ROJO+'El dinero que ingreso debe ser menor a 100000 y mayor a 1 porfavor ingrese una cantidad valida')
        pozo = int(input(BLANCO+'Cuanto dinero quiere destinar al pozo: \n'+BLANCO))
    pdrSuma = pozo
    PDRcontador = 1
    #declaramos funciones
    def borrador_pantalla ():
        print(input(AZUL+'\nSe borrara todo lo que haya escrito en la consola\nPresione enter para continuar...')+BLANCO)
        os.system ("cls")
    def borrador_sin_preguntar():
        os.system ("cls")
    def apostar(apuesta:int):   #AQUI DEFINIMOS EL FUNCIONAMIENTO DE LAS APUESTAS
        while apuesta > pozo or apuesta < 1:
            print(ROJO+'No puede apostar esa cantidad.\tel pozo actual es de: '+str(pozo))
            apuesta = int(input(BLANCO+'Cuanto dinero quiere apostar: '))
        return apuesta
    
    def menu():
        print("\n"+CYAN+separador+"\n")      #AQUI DEFINIMOS EL FUNCIONAMIENTO DEL MENU
        print ("-"*(30-9), "Menu de Opciones", "-"*(30-9), "\n")
        print(f"\nTu dinero actual del pozo es de {pozo}\n")
        print('Opcion 1: RECARGAR \nOpcion 2: JUGAR UNA MANO \nOpcion 3: SALIR')
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

    def verificarGanador(sumaJugador, contadorDeCartasDeJugador, sumaCrupier, contadorDeCrupier, apuesta):
        if sumaJugador > sumaCrupier and sumaJugador <= 21:
            print(separador_ganador_jugador)
            print(VERDE+f"Has ganado ahora se te sumaran tu {apuesta}"+BLANCO)
            return True
        elif sumaCrupier > sumaJugador and sumaCrupier <= 21:
            print(separador_ganador_croupier)
            print(ROJO+f"Has perdido contra el Croupier, se te restaran tu {apuesta} "+BLANCO)
            return False
        elif sumaJugador == sumaCrupier and sumaJugador <= 21:
            if contadorDeCartasDeJugador == 2 and contadorDeCrupier == 2:
                print(separador_ganador_croupier)
                print(ROJO+"perdes contra el crupier al obtener el mismo BlackJack Ntural que el crupier"+BLANCO)
                return False
            elif contadorDeCartasDeJugador == 2 and contadorDeCrupier != 2 :
                print(separador_ganador_jugador)
                print(VERDE+f"Has Ganado Al tener BlackJack Natural contra el Croupier, se te sumara la apuesta de {apuesta}"+BLANCO)
                return True
            elif contadorDeCartasDeJugador != 2 and contadorDeCrupier == 2:
                print(separador_ganador_croupier)
                print(ROJO+f"Los dos obtuvieron el mismo BlackJack, pero el crupier obtuvo el blackJack Natural asi que se te restara tu {apuesta}"+BLANCO)
                return False
            elif contadorDeCartasDeJugador != 2 and contadorDeCrupier != 2:
                print(separador_ganador_croupier)
                print(ROJO+f"Has empatado contra el Croupier, pero lo mismo pierdes tu apuesta de {apuesta}"+BLANCO)
                return False
        else:
            print(ROJO+f"Has perdido contra el Croupier, pero lo mismo pierdes tu apuesta de {apuesta}"+BLANCO)
            return False

    op = True
    
    while op != 3:
        if seguidos:
            seguidillaContador += 1
            print(AMARILLO+f"vas {seguidillaContador} partidas ganadas seguidas"+BLANCO)
        else:
            seguidillaContador = 0
        if banderaSeguidilla or seguidillaContador > mayRacha:
            mayRacha = seguidillaContador
            banderaSeguidilla = False
        borrador_sin_preguntar()
        if bandera or mayPozo < pozo:
            mayPozo = pozo
            bandera = False
        op = menu()
        borrador_sin_preguntar()
        #menu options
        if op == 1:
            recargaAlPozo = int(input('\nCuanto dinero quiere recargar: '))
            while recargaAlPozo > 100000 or recargaAlPozo < 1:
                print(ROJO+'\nEl dinero que pusiste es negativo o mayor a 100000, por favor ingrese un valor menor\n')
                recargaAlPozo = int(input(BLANCO+'Cuanto dinero quiere recargar?: '))
            pdrSuma += recargaAlPozo     #promedio de recarga al pozo
            PDRcontador +=1
            pozo += recargaAlPozo
            borrador_sin_preguntar()
        elif op == 2:
            print("-"*10+" Juego "+"-"*10)
            apuesta = apostar(int(input('\nCuanto dinero quiere apostar: ')))
            borrador_pantalla ()
            print('Tus cartas son:\n')
            c1_jugador = generar_carta()
            c2_jugador = generar_carta()
            sumaJugador = suma_cartas(c1_jugador,c2_jugador)
            #Suma Jugador
            print(f"\nLa Suma de {jugador} Cartas es: {sumaJugador} \n")
            print(separador+"\n")
            #Parte Croupier
            print("La Primera Carta del Crupier es:\n")
            c1_crupier = generar_carta()
            suma_Crupier = c1_crupier
            #Pregunta para seguir generando cartas Jugador
            #contador de cartas
            banderaNatural = True
            contadorDeCartasDeJugador= 2
            contadorDeCrupier= 1
            borrador_pantalla ()
            print("\n"+separador+"\n")
            seguir = input(f"{jugador} Desea pedir otra carta? (Presione s = (si)/ n = (no) ): ")
            #Ciclo donde se genera una nueva carta al jugador
            while seguir != "n":
                carta_jugador = generar_carta()
                sumaJugador = suma_cartas(sumaJugador,carta_jugador)
                contadorDeCartasDeJugador += 1
                #?se restas la suma cuando salga el as de 11 a 1
                if c1_jugador == 11 and sumaJugador>21:
                    sumaJugador -= 10
                    print('El As de la primera mano vale ahora 1')
                if c2_jugador==11 and sumaJugador >21:
                    sumaJugador -=10
                    print('El As de la segunada mano vale ahora 1')
                if sumaJugador == 21:
                    print(f"{jugador} Sacaste 21\n")
                    break
                elif sumaJugador < 21:
                    print(f"{jugador} La suma total de tus cartas es: {sumaJugador}\n")
                    seguir = input("Desea pedir otra carta (presione s=(si)/n=(no)): ")
                else:
                    print(f"Te pasaste de 21\ntu suma es {sumaJugador}\n")
                    break
            print(separador+"\n")
            borrador_pantalla()
            #parte del crupier para ver si toma o no cartas
            while suma_Crupier <= 16:
                carta_crupier_generica = generar_carta()
                print("El Croupier Pidio otra Carta\n")
                suma_Crupier = suma_cartas(suma_Crupier,carta_crupier_generica)
                if c1_crupier == 11 and suma_Crupier > 21:
                    suma_Crupier -= 10

                contadorDeCrupier += 1
                print(f"La suma total de las cartas del Crupier es: {suma_Crupier}\n")
                
                print('-'*60)

            print(f"\nEl crupier se planta con {suma_Crupier} puntos\n")
            borrador_pantalla ()
            primeraPartida = verificarGanador(sumaJugador, contadorDeCartasDeJugador, suma_Crupier, contadorDeCrupier, apuesta)
            if primeraPartida:
                seguidos = True
                pozo += apuesta
                print(VERDE+f"{jugador} tu pozo actual es de: {pozo}")
                winjugador += 1
                if contadorDeCartasDeJugador == 2 and sumaJugador == 21:
                    winNatural += 1
                    print(VERDE+f'{jugador} Gana con BlackJack Natural'+BLANCO)
                print(separador_ganador_jugador)
            else:
                seguidos = False
                pozo -= apuesta
                print(ROJO+f"{jugador} tu pozo actual es de: {pozo}")
                winCrupier += 1
                if contadorDeCrupier == 2 and suma_Crupier == 21:
                    winNatural += 1
                    print(ROJO+'El Croupier gana con BlackJack Natural'+BLANCO)
                    #Condiciones De ganadores
                print(separador_ganador_croupier)
            borrador_pantalla()
        vueltasDados += 1    
    print(f'cantidad de veces que gano el crupier {winCrupier}')
    print(f'cantidad de veces que gano el jugador {jugador} {winjugador}')
    print(f'cantidad de veces que se gano una mano por blackjack natural fue por {winNatural}')
    print(f'el valor maximo que alcanzo el pozo fue : {mayPozo}')
    print(f'la mayor racha seguida fue de {mayRacha}')
    print(f'el mondo promedio del pozo fue de {pdrSuma//PDRcontador}')
    borrador_pantalla()
main()