import random
random.seed(11)

multi4 = 0
multiAmbos = 0
suma = 0
cantMay2000 = 0
cantMayoralPrimerValor = 0
extremos= False
for i in range(1000):
    Aleterio = random.randint(1,2500)
    if i == 0:
        primerValor = Aleterio
    elif Aleterio > primerValor:
        cantMayoralPrimerValor +=1
    if Aleterio % 4 == 0 and Aleterio % 8 != 0:
        multi4 += 1
    elif Aleterio % 4 == 0 and Aleterio % 8 == 0:
        multiAmbos += 1
    if Aleterio > 2000:
        cantMay2000 += 1
        suma += Aleterio
    if Aleterio == 1 or Aleterio == 2500:
        extremos = True
print(multi4)
print(multiAmbos)
print(suma//cantMay2000)
print(cantMayoralPrimerValor)
if extremos:
    print("hubo un extremos")
else:
    print("no hubo extremo")