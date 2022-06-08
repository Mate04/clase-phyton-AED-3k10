__author__:"Franco Martina, Paredez Camila, Da silva Alexis, Loyola Ignacio"
import random
#Funciones
def verificador_de_num(n):
  if n > 100000:
    n=int(input("\nIngrese un valor correcto (debe ser menor a 100000): "))
  return n
def apostar(n1, n2):
  while n2 <= 0:
    n2=int(input("Ingrese un valor que sea mayor a 0: "))
  n1 += n2
  return n1
  
def opcion(op):
  while op <= 0 or op > 3:
    op=int(input("Eliga una opción correcta: "))
  return op
def cartas(n1,n2):
  n1 = ("AS",2,3,4,5,6,7,8,9,10,"J","Q","K")
  n2 = ("Diamante","Trébol","Pica","Corazón")
  n1 = random.choice(n1)
  n2 = random.choice(n2)
  return (n1,n2)
def verificador_carta(p):
  if p == "J" or p == "Q" or p == "K":
    p = int(10) 
  elif p == "AS":
    p = int(11)
  return p
def AS (bandera,AS):
  if AS == 11:
    bandera=False
  return bandera
def cambia_AS(bandera,sumatoria):
  if sumatoria > 21 and bandera == False:
    sumatoria -= 10
  return sumatoria
#Datos, Banderas, Separadores y Títulos 
separador="="
separador1="-"
bandera = natural = natural_c = primer_as_j = primer_as_c = True
monto = apuesta = pozo = vueltas = sum_c = sum_j = carta_j1 = agregar = natural = 0
carta = palo = carta_j = palo_j = carta_c  = palo_c = carta_c1 = palo_c1 = None
print(separador*60)
print("\t\t\t\t\tAguante el blackshack")
print(separador*60)
nombre= input("Ingrese su nombre: ")
monto = int (input("\nIngrese la cantidad de dinero a usar (No debe pasarse de 100.000$): "))
#Procesos
monto=verificador_de_num(monto)
print("\n\tOpcion 1:Apostar")
print("\tOpcion 2:Jugar a una mano")
print ("\tOpcion 3: Salir")
op = int(input("\nElija una opción: "))
op=opcion(op)

while op != 3:
  
  if op == 1 :
    pozo = int(input("Ingrese el dinero a agregar al monto (debe ser mayor a cero): "))
    monto = apostar(monto, pozo)
    print("El nuevo monto agregado es: ",monto)
    
  if op == 2:
    if monto != 0:
      apuesta=int(input("Ingrese el monto a postar:"))
      while apuesta <= 0 or apuesta%5 != 0 or apuesta > monto:
        apuesta=int(input("La puesta debe ser mayor a 0, multiplo de 5 y no mayor al monto: "))
      #cartas del jugador
        
      while vueltas != 2:
        carta_j, palo_j=cartas(carta_j, palo_j)
        carta_c , palo_c=cartas (carta_c,palo_c)
        vueltas += 1 
        
        print("La carta del jugador número",vueltas,"es",carta_j,"y su palo es",palo_j)
        
        if bandera:
          carta_c1=carta_c
          palo_c1=palo_c
          carta_j1=carta_j
          bandera=False
        if vueltas == 2:
          carta_c2=carta_c
          palo_c2=palo_c
          print("La carta del crupier número 1 es",carta_c1,"y su palo es",palo_c1)
        carta_j=verificador_carta(carta_j)
        carta_c=verificador_carta(carta_c)
        primer_as_j=AS(primer_as_j,carta_j)
        primer_as_c=AS(primer_as_c,carta_c)
        
        
        sum_j += carta_j
        sum_c += carta_c
      print ("\nSu sumatoria actual es ",sum_j)
      
      if sum_j < 21:
        agregar = int (input ("Si Desea otra carta presione 1 sino cualquier otro numero "))
        
        while agregar == 1:
          carta_j, palo_j=cartas(carta_j, palo_j)
          print("La nueva carta del jugador es",carta_j,"y su palo es",palo_j)
          carta_j=verificador_carta(carta_j)
          primer_as_j=AS(primer_as_j,carta_j)
          sum_j += carta_j
          sum_j=cambia_AS(primer_as_j,sum_j)
          print ("La sumatoria de las cartas actuales es de",sum_j)
          if sum_j >= 21:
            break
            agregar = int (input ("Si Desea otra carta presione 1 sino cualquier otro numero "))
        

      elif sum_j == 21:
        natural=False
      print ("La carta oculta del croupier era: ",carta_c2, "del palo", palo_c2)       
      while sum_c <= 16 :
        carta_c , palo_c=cartas(carta_c,palo_c)
        primer_as_c=AS(primer_as_c,carta_c)
        print("\nLa nueva carta del crupier es",carta_c,"y su palo es",palo_c)
        
        carta_c=verificador_carta(carta_c)
        sum_c += carta_c
        sum_c = cambia_AS (primer_as_c,sum_c)
        
      if (sum_c < 22 or sum_j < 22):
        
        if(sum_j >= 22):
          print ("\nEl jugador ha perdido")
          inicial = monto 
          monto -= apuesta
          
        elif(sum_c >= 22):
          print ("\nEl Crupier ha perdido")
          inicial = monto 
          monto += apuesta

        elif (sum_j == sum_c and natural == False and natural_c == False):
          print("\nAmbos jugadores han empatado por blackjack natural :(")
          inicial = monto
          
        elif (sum_j == sum_c and natural== False):
          print ("\n¡¡¡Felicidades usted ha ganado por blackjack Natural!!!")
          inicial = monto 
          monto += apuesta
          
        elif (sum_j == sum_c and natural_c == False):
          print ("\nPerdiste porque el Crupier tiene BlackJack natural :(")
          inicial = monto 
          monto -= apuesta
          
        elif (sum_j == sum_c):
          print("\nLos jugadores han empatado")
          
        elif (sum_j > sum_c):
          print ("\nEl jugador ha ganado")
          inicial = monto 
          monto += apuesta
          
          print("\nSu monto total ganado es:",monto)
          
        elif (sum_c > sum_j):
          print ("El crupier ha ganado")
          inicial = monto 
          monto -= apuesta
      else:
        print ("Ambos han perdido")
    else:
      print("No hay dinero en su monto,seleccione la opcion 1 para agregar dinero ",nombre)
  print("\n\tOpcion 1:Apostar")
  print("\tOpcion 2:Jugar a una mano")
  print ("\tOpcion 3: Salir")
  op = int(input("\nElija una opción: "))
  op=opcion(op)
