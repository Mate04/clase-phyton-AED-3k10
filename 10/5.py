import random
random.seed(29)

procesar = 10000
cantMay1 = 0
cantMay1000 =0
cantMay2000 = 0
cantDivis6 = 0
menor = True
sumTodoNumero = 0
for i in range(procesar):
    aleatorio = random.randint(1,25000)
    if 1 <= aleatorio < 10000:
        cantMay1 += 1
    if 10000 <= aleatorio < 20000:
        cantMay1000 += 1
    if 20000 <= aleatorio:
        cantMay2000 += 1
    if aleatorio % 6 == 0:
        cantDivis6 +=1
    if menor or menorNumber > aleatorio:
        menorNumber = aleatorio
        menor = False
    sumTodoNumero += aleatorio
print('mayor igual a 1 menor q 1000:',cantMay1)
print('mayor igual 1000 menor 2000:',cantMay1000)
print('mayor a 2000',cantMay2000)
print('cantidad divisible por 6:',cantDivis6)
print('el menor de todos los numeros:',menorNumber)
print('el promedio de estos numeros es de:',sumTodoNumero//procesar)