#insertar hora, minutos y segundos
hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
#convertir a segundos
segundosElegidos = hora * 3600 + minutos * 60 + segundos
#mostrar resultado
print(f"{segundosElegidos}")
# Compare this snippet from clase phyton\cuestionario_3\desafio.py:
# segundosElegidos = int(input("Cuantos segundos quieres convertir: "))
# hora = segundosElegidos // 3600
# minutos = (segundosElegidos % 3600) // 60
# segundos = (segundosElegidos % 3600) % 60
# print(f"{hora}:{minutos}:{segundos}")
#insertar hora, minutos y segundos
hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
#convertir a segundos
segundosElegidos = hora * 3600 + minutos * 60 + segundos
#mostrar resultado
print(f"{segundosElegidos}")

