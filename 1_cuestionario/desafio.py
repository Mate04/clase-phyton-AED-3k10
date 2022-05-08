segundosElegidos = int(input("Cuantos segundos quieres convertir: "))
hora = segundosElegidos // 3600
minutos = (segundosElegidos % 3600) // 60
segundos = (segundosElegidos % 3600) % 60
print(f"{hora}:{minutos}:{segundos}")