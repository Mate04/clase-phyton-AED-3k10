from random import randint
promedio = lambda sum,total: sum/total
lluviaAnual =lluviaTrimestral = [0]*12
n = sumaLluviaAnual=sumaLluviaTrimestral = c = 0
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
banderaMenor = True
for i in range(len(lluviaAnual)):
    #lluviaAnual[i] = int(input(f'ingrese el promedio de lluvia del mes {meses[i]}: '))
    lluviaAnual[i] = randint(1,10)
    sumaLluviaTrimestral += lluviaAnual[i]
    if (i+1) % 3 == 0:
        lluviaTrimestral[n] = promedio(sumaLluviaTrimestral,3)
        print(f'el trimestre numero {n+1} el promedio es de {lluviaTrimestral[n]}')
        sumaLluviaTrimestral = 0
        n+=1
    if banderaMenor or lluviaAnual[i] < menorMes[1]:
        menorMes = [i,lluviaAnual[i]]
        banderaMenor = False
    sumaLluviaAnual += lluviaAnual[i]
prom = promedio(sumaLluviaAnual,12) 
print(f'el promedio de lluvia en el año es de: {prom}')
print(f'el menor mes fue el mes {meses[menorMes[0]]}, y fue el promedio de {menorMes[1]}')
for i in range(len(lluviaAnual)):
    if lluviaAnual[i] >= prom:
        c += 1
mayorPromedio = c * [0]
aux = 0
for i in range(len(lluviaAnual)):
    if lluviaAnual[i] >= prom:
        mayorPromedio[aux] = lluviaAnual[i]
        aux += 1
print('los meses con mayor promedio fueron: ')
for i in range(len(mayorPromedio)):
    print(mayorPromedio[i])