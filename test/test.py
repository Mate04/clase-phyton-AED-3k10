lista = [[1,2,3,4],[4,5,6],[7,9,9]]
vuelta = vuelta2= c = 0
for i in range(len(lista)):
    vuelta2 = 0
    for j in lista[i]:
        if j == lista[i][2] and vuelta2 == 2:
            c += lista[i][2]
            vuelta += 1
        vuelta2 += 1
print(c/vuelta)
print(8.5)