ascendente = []
constador = 0
option = True
cont1 = 0
while option != 0:
    option = int(input('Ingresar una carga de numero finaliza en 0\n'))
    if option % 2 != 0:
        ascendente.append(option)
    else:
        ascendente.clear()
    if len(ascendente) == 3:
        if ascendente[0] > ascendente[1] or ascendente[1] > ascendente[2]:
            ascendente.pop(0)
        else:
            constador += 1
            ascendente.clear()
    print("ascendente",constador)