#insertar hora, minutos y segundos
hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
#convertir a segundos
segundosElegidos = hora * 3600 + minutos * 60 + segundos
#mostrar resultado
print(f"{segundosElegidos}")


