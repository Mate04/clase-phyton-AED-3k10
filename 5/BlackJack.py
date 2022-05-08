__author__ = "Mateo Maldonado 98717, Lucas Cuello Arrigoni 92765, Matias Sciarra 95034"
#INICIO DEL PROGRAMA #Importamos Random para elegir aleatoriamente
import random
#Importaciones de colores para que todo se vea más lindo
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

print(YELLOW+"Bienvenido al juego del BlackJack")
#INGRESO DEL NOMBRE DEL JUGADOR
nombre = input(MAGENTA+"Ingrese su nombre: \n")
#PALOS DE LAS CARTAS
palos = ("Treboles", "Corazones", "Diamantes", "Picas")
valores =("As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
#para hacer las lineas
Separador= '_' *60
#COMIENZO DEL JUEGO
a = int(input(BLUE+"Hola " + nombre + ", desea comenzar? \n 1-Si \n 2-No\n"))
if a == 1:
    #declaramos un booleano para saber si toco un palo
    bandera = False
    #Declaramos variable Globales para mas adelante asignarle el valor final del puntaje
    puntuacionFinalJugador = None
    puntuacionFinalCrupier = None
    #cartas del Crupier dando
    c1Crupier = [random.choice(valores), random.choice(palos)]
    c2Crupier = [random.choice(valores), random.choice(palos)]
    print(GREEN+Separador,"\n","La cartas del Crupier son:\n", c1Crupier[0], "de", c1Crupier[1],
          "y", c2Crupier[0], "de", c2Crupier[1])
    #Aca estamos convirtiendo las figuras a valores de numeros, para asi poder sumarlos
    if c1Crupier[0] == "K" or c1Crupier[0] == "Q" or c1Crupier[0] == "J":
        bandera = True
        c1Crupier[0] = 10
    if c2Crupier[0] == "K" or c2Crupier[0] == "Q" or c2Crupier[0] == "J":
        bandera = True
        c2Crupier[0] = 10
    #Si toca dos As vale 1 Sino 11
    if c1Crupier[0] == "As" and c2Crupier[0] == "As":
        c1Crupier[0] = 11
        c2Crupier[0] = 1
    elif c1Crupier[0] == "As":
        c1Crupier[0] = 11
    elif c2Crupier[0] == "As":
        c2Crupier[0] = 11
    sumaCrupier = c1Crupier[0]+ c2Crupier[0] #Esta es la suma de las 2 primeras cartas del Crupier
    print("La suma de las dos primeras cartas del Crupier da:",sumaCrupier)
    print(Separador)
    #cartas del jugador
    baraja1Jugador = [random.choice(valores), random.choice(palos)]
    baraja2Jugador = [random.choice(valores), random.choice(palos)]
    print(YELLOW+Separador,"\n","La cartas de",nombre, "son:\n", baraja1Jugador[0], "de", baraja1Jugador[1],
          "y", baraja2Jugador[0], "de", baraja2Jugador[1])
    #Cambiamos los String de K, Q, J de la baraja 1 y baraja 2 a 10
    if baraja1Jugador[0] == "K" or baraja1Jugador[0] == "Q" or baraja1Jugador[0] == "J":
        bandera = True
        baraja1Jugador[0] = 10
    if baraja2Jugador[0] == "K" or baraja2Jugador[0] == "Q" or baraja2Jugador[0] == "J":
        bandera = True
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
    print("la suma de",nombre, "es:",sumaJugador,"\n", Separador)
    b = input(GREEN+"Por favor, " + nombre + ", presione cualquier tecla para continuar y presione enter\n")
    print(WHITE, Separador)
    #Comparador de los palos
    if baraja1Jugador[1] == c1Crupier[1]:
      print(YELLOW+Separador,"\n","Tu primer carta con la del crupier coinciden en palos","\n",Separador)
      #Ahora si coinciden tambien en numero
      if baraja1Jugador[0] == c1Crupier[0]:
        print("Tambien coinciden en numero")
    #Este es un comparador por si las cartas tienen figuras como "J","Q" o "K"
    elif (baraja1Jugador[0] == 10 or baraja1Jugador[0] == 11 or baraja1Jugador[0] == 12) and (c1Crupier[0] == 10 or c1Crupier[0] == 11 or c1Crupier[0] == 12):
      print(BLUE+"La primer carta tuya con la del crupier tienen figuras","\n")
    #si la suma del crupier es mayor o igual a 17 alza una tercera carta
    if sumaCrupier >= 17: 
      #si la suma del jugador es mayor o igual a 17 alza una tercera carta
      if sumaJugador >= 17:
        print(YELLOW+"\n"+"El crupier y tu se han pasado de 17 por lo tanto no se les dara mas cartas a cada uno","\n")
        #comparamos ganadores
        if sumaJugador == sumaCrupier:
          print("Han empatado")
        elif sumaJugador > 21:
          print("Has perdido, te has pasado de 21")
        elif sumaCrupier > 21 or ((21 - sumaCrupier) > (21 - sumaJugador)):
          print(CYAN+"Felicitaciones, has ganado!!!")
        else:
          print(RED+"Lo siento pero has perdido")
      else: #Este es el caso en el cual el Crupier tiene puntuacion mayor a 17 pero vos no
        print(BLUE+"El Crupier ha igualado o se ha pasado de 17, pero vos no, asi que ahora tendras otra carta")
        baraja3Jugador = [random.choice(valores), random.choice(palos)]
        print(MAGENTA+"Tu tercera carta es", baraja3Jugador[0], "de", baraja3Jugador[1])
        if baraja3Jugador[0] == "K" or baraja3Jugador[0] == "Q" or baraja3Jugador[0] == "J":
          bandera = True
          baraja3Jugador[0] = 10
        elif baraja3Jugador[0] == "As":
          baraja3Jugador[0]= 11
        finalJugador = (sumaJugador + baraja3Jugador[0])
        print(YELLOW+"La suma final de tus 3 cartas es",finalJugador)
        #Se decide aca quien es el ganador
        if finalJugador == sumaCrupier:
          print(GREEN+"Han empatado")
        elif finalJugador > 21:
          print(RED+"Has perdido, te has pasado de 21")
        elif sumaCrupier > 21 or ((21 - sumaCrupier) > (21 - finalJugador)):
          print(BLUE+"Has ganado!!!!")
        else:
            print(RED+"Has perdido")
    else: #Este es el camino que se toma cuando la suma de las cartas del Crupier son menores a 17
      print(GREEN+"El crupier no llega a los 17 puntos por lo tanto ahora se le dara otra carta")
      c3crupier = [random.choice(valores), random.choice(palos)]
      print(BLUE+"La tercera carta del crupier es", c3crupier[0], "de", c3crupier[1])
      if c3crupier[0] == "K" or c3crupier[0] == "Q" or c3crupier[0] == "J":
        bandera = True
        c3crupier[0] = 10
      elif c3crupier[0] == "As":
        c3crupier[0]= 11
      finalCrupier = (sumaCrupier + c3crupier[0])
      print(MAGENTA+"La suma total de las 3 cartas del Crupier es",finalCrupier)
      if sumaJugador >= 17:
        print("Como vos igualaste o te pasaste de los 17 no podes pedir otra carta")
        if sumaJugador == finalCrupier:
          print(GREEN+"Han empatado")
        elif sumaJugador > 21:
          print(RED+"Has perdido, te has pasado de 21")
        elif finalCrupier > 21 or ((21 - finalCrupier) > (21 - sumaJugador)):
          print(YELLOW+"Has ganado!!!!!")
        else:
            print(RED+"Has perdido")
      else:
        print(CYAN+"Como vos no llegaste a 17 en tus primeras dos cartas se te dara otra carta")
        baraja3Jugador = [random.choice(valores), random.choice(palos)]
        print("\033[0;33m","tu tercera carta es", baraja3Jugador[0], "de", baraja3Jugador[1] )
        if baraja3Jugador[0] == "K" or baraja3Jugador[0] == "Q" or baraja3Jugador[0] == "J":
          baraja3Jugador[0] = 10
        elif baraja3Jugador[0] == "As":
          baraja3Jugador[0]= 11
        finalJugador = (sumaJugador + baraja3Jugador[0])
        print(MAGENTA+"Tu puntuacion final es",finalJugador)
        if finalJugador == finalCrupier:
          print(GREEN+"Han empatado, los dos llegaron a la puntuación de", finalJugador)
        elif finalJugador > 21:
          print(RED+"Has perdido, que lastima, ya que te has pasado de 21")
        elif finalCrupier > 21 or ((21 - finalCrupier) > (21 - finalJugador)):
          print(YELLOW+"Has ganado!!!!")
        else:
          print(RED+"Has perdido")
#cuando elegimos un numero distinto a 1 o 0 al comienzo del juego
elif a != 1 and a != 0:
  print(RED+"Se cierra el juego...")
else:
  print(MAGENTA+"Nos vemos")
print(CYAN,Separador)
if c1Crupier[0] == baraja1Jugador[0] and c1Crupier[1] == baraja1Jugador[1]:
    print("Las cartas del crupier y del jugador son iguales tanto el palo como el valor\n ")
elif c1Crupier[0] == baraja1Jugador[0]:
    print("Las cartas del crupier y del jugador son iguales en el valor pero no en el palo\n ")
elif c1Crupier[1] == baraja1Jugador[1]:
    print("Las cartas del crupier y del jugador son iguales en el palo pero no en el valor\n ")
if bandera:
  print("Hubo almenos una figura en toda la partida")
print(Separador)