"""
Ordenar y buscar
Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive (pueden existir duplicados). A partir de ese arreglo:

Ordenarlo de forma ascendente y mostrarlo
Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si existe, determinar cuántos valores impares mayores a x se encontraron en el arreglo.
"""
import random

def ordenar(vect):
    n=len(vect)
    for i in range(n-1):
        for j in range(i+1,n):
            if vect[i]> vect[j]:
                vect[i], vect[j]= vect[j] ,vect[i]
    return vect
def buscar(vect, x):
    bandera = False
    vuelta = 0
    posicion = None
    for i in vect:
        if i == x:
            bandera = True
            posicion = vuelta
        vuelta += 1
    return [bandera, posicion]
def imparesMayores(vect, x):
    vectorNuevo = []
    for i in vect:
        if (i % 2 != 0) and x < i:
            vectorNuevo.append(i)
    return vectorNuevo
def principal():
    v1 = []
    n = int(input('cuanto elementos quieren cargar en el vector'))

    for i in range(n):
        elemento = random.randint(1,100)
        v1.append(elemento)
    print(v1)
    vectorOrdenado = ordenar(v1)
    print(vectorOrdenado)
    #punto 2
    x = int(input("que elemento quiere buscar "))
    resultado = buscar(vectorOrdenado,x)
    if resultado[0]:
        vectorImparMay = imparesMayores(vectorOrdenado, x)
        print(f'Se encontro resultado en la posicion {resultado[1]}\ny los elementos impares mayores al resulrtado son {vectorImparMay}')
    else:
        print('no se encontro resultado')
principal()