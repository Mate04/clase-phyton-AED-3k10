__author__ = "Mateo Maldonado 98717, Lucas Cuello Arrigoni 92765, Matias Sciarra"
#INICIO DEL PROGRAMA
import random
print("\033[0;36m"+"bienvenido al juego del BlackJack")
#INGRESO DEL NOMBRE DEL JUGADOR
nombre = input("\033[0;31m"+"Ingrese su nombre: \n")
#PALOS DE LAS CARTAS
palos = ["Treboles", "Corazones", "Diamantes", "Picas"]
Separador= '_' *60
valores = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#COMIENZO DEL JUEGO
a = int(input("\033[0;37m"+"Hola " + nombre + ", desea comenzar? \n 1-Si \n 2-No\n"))
if a == 1:
    #Declaramos variable Globales para mas adelante asignarle el valor final del puntaje
    puntuacionFinalJugador = None
    puntuacionFinalCrupier = None
    #cartas del Crupier dando
    c1_crupier = [random.choice(valores), random.choice(palos)]
    c2Crupier = [random.choice(valores), random.choice(palos)]
    print("\033[0;35m",Separador,"\n","La cartas del Crupier son:\n", c1_crupier[0], "de", c1_crupier[1],
          "y", c2Crupier[0], "de", c2Crupier[1])
    #Cartas del crupier
    if c1_crupier[0] == "K" or c1_crupier[0] == "Q" or c1_crupier[0] == "J":
        c1_crupier[0] = 10
    if c2Crupier[0] == "K" or c2Crupier[0] == "Q" or c2Crupier[0] == "J":
        c2Crupier[0] = 10
    #Si toca dos As vale 1 Sino 11
    if c1_crupier[0] == "As" and c2Crupier[0] == "As":
        c1_crupier[0] = 11
        c2Crupier[0] = 1
    elif c1_crupier[0] == "As":
        c1_crupier[0] = 11
    elif c2Crupier[0] == "As":
        c2Crupier[0] = 11
    sumaCrupier = c1_crupier[0]+ c2Crupier[0]
    print("\033[0;35m","La suma de las dos primeras cartas del Crupier da:",sumaCrupier)
    print(Separador)
    #cartas del jugador
    baraja1Jugador = [random.choice(valores), random.choice(palos)]
    baraja2Jugador = [random.choice(valores), random.choice(palos)]
    print("\033[0;33m",Separador,"\n","La cartas de",nombre, "son:\n", baraja1Jugador[0], "de", baraja1Jugador[1],
          "y", baraja2Jugador[0], "de", baraja2Jugador[1])
    #Cambiamos los String de K, Q, J de la baraja 1 y baraja 2 a 10
    if baraja1Jugador[0] == "K" or baraja1Jugador[0] == "Q" or baraja1Jugador[0] == "J":
        baraja1Jugador[0] = 10
    if baraja2Jugador[0] == "K" or baraja2Jugador[0] == "Q" or baraja2Jugador[0] == "J":
        baraja2Jugador[0] = 10
    #Si toca dos As vale 1 Sino 11
    if baraja1Jugador[0] == "As" and baraja2Jugador[0] == "As":
        baraja1Jugador[0] = 11
        baraja2Jugador[0] = 1
    elif baraja1Jugador[0] == "As":
        baraja1Jugador[0] = 11
    elif baraja2Jugador[0] == "As" :
        baraja2Jugador[0] = 11
    sumaJugador = baraja1Jugador[0]+baraja2Jugador[0]
    print("\033[0;33m","la suma de",nombre, "  es : ",sumaJugador,"\n", Separador)
    b = int(input("\033[0;37m"+"porfavor "+nombre+ ", presione 1 para Continuar\n"))
    #Parte Final Crupier
    print("\033[0;35m",Separador)
    if sumaCrupier == 21:
      print("\033[0;35m","La suma parcial de crupier",sumaCrupier)
      puntuacionFinalCrupier = sumaCrupier
    elif sumaCrupier < 21:
      c3crupier = [random.choice(valores), random.choice(palos)]
      print("\033[0;35m","la tercera carta del crupier es", c3crupier[0], "de", c3crupier[1] )
      if c3crupier[0] == "K" or c3crupier[0] == "Q" or c3crupier[0] == "J":
        c3crupier[0] = 10
      elif c3crupier[0] == "As":
        c3crupier[0]= 11
      finalCrupier = (sumaCrupier + c3crupier[0])
      print("\033[0;35m","la puntuacion Final del crupier es",finalCrupier)
      puntuacionFinalCrupier = finalCrupier
    else:
      print("\033[0;35m","Perdio el crupier a la primera",sumaCrupier)
      puntuacionFinalCrupier = sumaCrupier
    print(Separador)
    #PARTE FINAL JUGADOR
    print("\033[0;33m",Separador)
    if sumaJugador == 21:
      print("\033[0;33m","tu puntacion fue",sumaJugador)
      puntuacionFinalJugador = sumaJugador
    elif sumaJugador < 21:
      baraja3Jugador = [random.choice(valores), random.choice(palos)]
      print("\033[0;33m","tu tercera carta es", baraja3Jugador[0], "de", baraja3Jugador[1] )
      if baraja3Jugador[0] == "K" or baraja3Jugador[0] == "Q" or baraja3Jugador[0] == "J":
        baraja3Jugador[0] = 10
      elif baraja3Jugador[0] == "As":
        baraja3Jugador[0]= 11
      finalJugador = (sumaJugador + baraja3Jugador[0])
      print("\033[0;33m","tu puntuacion Final es",finalJugador)
      if finalJugador > 21:
        print("\033[0;33m","Perdiste tu puntuacion final fue", finalJugador)
      puntuacionFinalJugador = finalJugador
    else:
      puntuacionFinalJugador = finalJugador
      print("\033[0;33m","Perdiste a la primera tu puntuacion quedo en",finalJugador)
    print(Separador)
    #Comparamos Puntajes
    if puntuacionFinalCrupier <= 21 and puntuacionFinalJugador <= 21:
      if puntuacionFinalCrupier < puntuacionFinalJugador:
        print('\033[0;32m',Separador,'\n','Ganaste',nombre,'!!!👍😎👌')
      else:
        print("\033[0;31m",Separador,"\n","Gano el Crupier😭")
    elif puntuacionFinalJugador <= 21:
      print('\033[0;32m',Separador,'\n','Ganaste',nombre,'!!!👍😎👌')
    elif puntuacionFinalCrupier <= 21:
      print("\033[0;31m",Separador,"\n","Gano el Crupier😭")
    elif puntuacionFinalCrupier >21 and puntuacionFinalJugador >21:
      print("\033[0;37;40m","los dos pierden 😭")
    print(Separador)
elif a != 1 and a != 0:
  print("se cierra el juego...nos vemos")
else:
  print("Nos vemos")