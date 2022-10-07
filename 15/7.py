import random
def promedio(a,b):
    if b != 0:
        return a//b
    else:
        return 'No se puede dividir entre 0'
def ordenar(a:list,posicion:int):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j][posicion] > a[j+1][posicion]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
dia = 1
listadoDeTransporte = []
c = 0
for i in range(31):
    descripcion = ['flor','pao','mateo','juan']
    montoDeTransporte = random.randint(0,100)
    listaAuxiliar = [dia, descripcion[random.randint(0,3)],montoDeTransporte]
    listadoDeTransporte.append(listaAuxiliar)
    dia += 1
for i in range(len(listadoDeTransporte)):
    c += listadoDeTransporte[i][2]
#Determinar el dia que tuvo mayor ganancia
mayorGanancia = 0
for i in range(len(listadoDeTransporte)):
    if listadoDeTransporte[i][2] > mayorGanancia:
        mayorGanancia = listadoDeTransporte[i][2]
        diaMayorGanancia = listadoDeTransporte[i][0]
#Genere un listado de los envíos realizados, ordenado por importe en forma decreciente sin usar sort
listadoDeTransporte.sort(key=lambda x: x[2], reverse=True)
#ordene de menor a mayor sin usar sort
op = True
while op != 0:
    op = int(input('1. mostrar array\n2. Dia de mayor ganancia\n3. Promedio\n4. Ordenamiento\n0. Salir\n'))
    if op == 1:
        for i in range(len(listadoDeTransporte)):
            print(listadoDeTransporte[i])
    elif op == 2:
        print(f'El dia {diaMayorGanancia} tuvo mayor ganancia con un total de {mayorGanancia}')
    elif op == 3:
        print(f'el promedio fue de',promedio(c,31))
    elif op == 4:
        print(ordenar(listadoDeTransporte,2))