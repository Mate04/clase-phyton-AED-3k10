promedio = lambda promedio, cant: promedio / cant
n = int(input('cantidad de lineas '))
m = int(input('cantidad de paradas '))
arrayCombiando =[]
for i in range(n):
    arrayCombiando.append([])
    for j in range(m):
        c = int(input(f'cuantos pasajeros se subieron en la linea {i} en la parada {j}: '))
        arrayCombiando[i].append(c)
#inicializamos variables
paradaProm = int(input('que promedio de pasajeros que se tomaron para la parada'))
punto2 = vuelta2= vuelta3 = 0
punto3 = []
punto4 = 0
for i in range(len(arrayCombiando)):
    #inicializamos variables
    punto1 = vuelta =  0
    for j in arrayCombiando[i]:
        #punto 1
        punto1 += j
        #punto 2
        if j == arrayCombiando[i][paradaProm] and vuelta == paradaProm:
            punto2 += arrayCombiando[i][paradaProm]
            vuelta2 +=1
        vuelta += 1
    punto3.append(punto1)
    #punto 4
    punto4 += punto1*8.5
    #imprimimos las salidas
    print(f'la linea {i} tuvo {punto1} pasajeros')
#punto 3
bandera = True
for i in punto3:
    if bandera or menor > punto3[vuelta3]:
        menor = i
        posicion = vuelta3
        bandera = False
    vuelta3+=1
print(f'el promedio de la parada de pasajeros fue de {promedio(punto2,vuelta2)}')
print(f'la linea {posicion} tuve la menor cantidad de pasajeros')
print(f'la empresa recaudo {punto4} pesos')