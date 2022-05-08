# while = mientras
n1 = int(input("un numero diferente a cero: "))
contador = 0
while n1 != 0:
    if contador != 0:
        n1 = int(input("un numero diferente a cero(dentro del while): "))
    contador += 1
    print("hola mundo")
    if n1 == 5:
        pass
#while contador < 10:
print("codigo repitio:", contador)
#   print("hola")
#  contador += 1
