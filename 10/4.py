import random
random.seed(11)

options = True
contador4but8dont = 0
contador4but8 = 0
contadorPromedio = 0
sumPromedio = 0
bandera = True
contPrimerValor = 0
vueltas = 1000
for i in range(vueltas):
    options = random.randint(1,2500)
    if bandera:
        primerValor = options
        bandera = False
    elif primerValor > options:
        contPrimerValor += 1
    if options % 4 == 0 and options % 8 !=0:
        contador4but8dont +=1
    elif options % 4 == 0 and options % 8 ==0:
        contador4but8 += 1
    if options > 2000:
        contadorPromedio += 1
        sumPromedio += options
    if options == 1 or options == 2500:
        print('aperecio un extremo:',options)
print(contador4but8dont)
print(contador4but8)
print(sumPromedio/contadorPromedio)
print((contPrimerValor*100)/vueltas)

