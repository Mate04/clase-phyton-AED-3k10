NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'

separador_ganador_croupier = '<'*30 + '>'*30
separador = "="*60
separador_ganador_jugador = "*"*60
separador_empate = "+"*60

pozo =10000
apuesta= 5000
banderaNatural = True

winjugador = 0
winCrupier = 0
winNatural = 0
#*jugador
sumaJugador= 20
contadorDeCartasDeJugador = 2
#*crupier
suma_Crupier = 19
contadorDeCrupier = 2

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
        elif sumaJugador <= 21 and sumaCrupier > 21:
            print(separador_ganador_jugador)
            print(VERDE+f"Has ganado ahora se te sumaran tu {apuesta}"+BLANCO)
            return True
        elif sumaJugador > 21 and sumaCrupier <= 21:
            print(separador_ganador_croupier)
            print(ROJO+f"Has perdido contra el Croupier, se te restaran tu {apuesta} "+BLANCO)
            return False
        else:
            print(separador_ganador_croupier)
            print(ROJO+f"Has perdido contra el Croupier, se te restaran tu {apuesta} "+BLANCO)
            return False

primeraPartida = verificarGanador(21, contadorDeCartasDeJugador, 19, contadorDeCrupier, apuesta)
if primeraPartida:
    pozo += apuesta
    print(VERDE+f"Tu pozo actual es de: {pozo}")
    winjugador += 1
    if contadorDeCartasDeJugador == 2 and sumaJugador == 21:
        winNatural += 1
        print(VERDE+'El jugador gana con BlackJack Natural'+BLANCO)
else:
    pozo -= apuesta
    print(ROJO+f"Tu pozo actual es de: {pozo}")
    winCrupier += 1
    if contadorDeCrupier == 2 and suma_Crupier == 21:
        winNatural += 1
        print(ROJO+'El Croupier gana con BlackJack Natural'+BLANCO)



#if sumaJugador > suma_Crupier and sumaJugador <= 21:
#    pozo += apuesta
#    winjugador += 1
#    print(VERDE+separador_ganador_jugador)
#    print(f"Has ganado ahora se te sumaran {apuesta}\t tu pozo actual es de: {pozo}")
#    print(separador_ganador_jugador+BLANCO)    
##Cuando Empatan
#elif sumaJugador == suma_Crupier and sumaJugador <= 21:
#    if sumaJugador == 21:
#        if co_cjugador == 2 and co_ccrupier == 2:
#        #? si ambos obtienen blackjack natural, empatan o gana crupier?
#            print(separador)
#            print("Ambos empatan al tener BlackJack Ntural")
#            print(separador)
#            banderaNatural = False
#        elif co_cjugador == 2 and co_ccrupier != 2 :
#            #GANAMOS BlackJack
#            print(separador_ganador_jugador) 
#            print(VERDE+"Has Ganado Al tener BlackJack Natural contra el Croupier")
#            print(separador_ganador_jugador)
#            winjugador += 1
#            banderaNatural = False
#            winNatural += 1
#        elif co_cjugador != 2 and co_ccrupier == 2:
#            winCrupier += 1
#            winNatural += 1
#            banderaNatural = False
#        #PERDIMOS
#            print(separador_ganador_croupier)
#            print(ROJO+"Has Perdido contra el Croupier obtuvo BlackJack Natural")
#            print(separador_ganador_croupier)
#        #!:Preguntar Hacer la condicion si ambos tuvieron 21 pero no blackjack natural
#    else:
#    #EMPATAMOS
#        print(separador_empate)
#        print("Empate")
#        print(separador_empate)
#    #print(f"Empataron los dos tuvieron un puntaje de {suma_Crupier}\n")
#    #Cuando Pierde
##Gana Croupier    
#elif sumaJugador < suma_Crupier and suma_Crupier <= 21:
#    pozo -= apuesta
#    winCrupier += 1
#    print(separador_ganador_croupier)
#    print(ROJO+f"Has perdido contra el Croupier, se te restaran {apuesta} tu pozo actual va a ser {pozo}\n")
#    print(separador_ganador_croupier)
##Ambos se pasaron de 21  
#else:
#    print(ROJO+separador_ganador_croupier)
#    print(f"Has perdido contra el Croupier, se te restaran {apuesta} tu pozo actual va a ser {pozo}\n")
#    print(separador_ganador_croupier+BLANCO)
#    winCrupier += 1
##esta linea se ejecuta solo y solo si no se ejecuto el bloque anterior de empate del blackjack natural
#if banderaNatural:
#    if co_ccrupier ==2 and suma_Crupier == 21:
#        print(ROJO+"El Croupier obtuvo BlackJack Natural")
#        print(separador_ganador_croupier+BLANCO)
#        winNatural += 1
#    elif co_cjugador == 2 and sumaJugador == 21:
#        print(VERDE+"El jugador hizo un BlackJack Natural")
#        print(separador_ganador_jugador+BLANCO)
#        winNatural += 1