sets = int(input('ingrese la cantidad de sets (3,5): '))
while sets not in [3,5]:
    sets = int(input('ingrese la cantidad de sets (3,5): '))
jugador1 = input('ingrese el nombre del jugador 1: ')
jugador2 = input('ingrese el nombre del jugador 2: ')
jugadores = [jugador1, jugador2]
vector = []
for i in range(2):
    vector.append([])
    for j in range(sets):
        vector[i].append(input(f'ingrese el resultado del set {j+1} del jugador {jugadores[i]}: '))
for i in range(sets):
    if vector[0][i] == vector[1][i]:
        print('empate')
    elif vector[0][i] > vector[1][i]:
        print(f'{jugador1} gana el set {i+1}')
    else:
        print(f'{jugador2} gana el set {i+1}')
print(vector)