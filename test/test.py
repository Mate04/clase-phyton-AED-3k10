"""
def verificarLinea(vect:list,listNum:list):
    for i in vect:
        if i not in listNum:
            return False
    return True
def matrizTransVersal(m:list):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez
print(matrizTransVersal([[3,4,5],[3,4,6]]))
"""

contador = [[3,4,89,65,32],[2,5,6],[3,4,5]]
Tematica1 = contador[0]
vueltas = 0
banderaMayor = True
for i in Tematica1:
    if banderaMayor or may < i:
        may = i
        posicion = vueltas
        banderaMayor= False
    vueltas += 1
print(f'el numero mayor de la tematica 1 es {may}, y esta en la posicion {posicion}')
print('el numero mayor es',may,'y su posicion es',posicion)