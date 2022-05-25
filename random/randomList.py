#hacer una lista random de personas 
#TODO: random utiliza para hacer random, agarra el reloj del sistema para q sea aleatorio
import random
listPersona = ["mateo", "Nacho", "Alex", "Luchacho", "marti","cami", "mati"]
print(listPersona)
#hacer una lista random de listPersonas
print(listPersona.__len__())
listRandom = random.sample(listPersona, listPersona.__len__())
print(listRandom)
