""""
1)Cantidad de palabras que empiezan con mayúscula.
2)Cantidad de números del 0 al 9 en todo el texto.
3)Cantidad de palabras que tienen más de una e.
4)Promedio de letras por palabra, para las palabras de longitud impar.
"""

def verificarText(text):
    while text[-1] != '.':
        text += '.'
    return text
def main():
    #Punto 1
    MAYUSC = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    cantMayus = 0
    #Punto 2
    NUMBER = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    cantNum = 0
    #Punto 3
    E = "E", "e"
    cantE = 0
    vueltaDadaE = False
    #Punto 4
    palabraImpar = 0
    sumaLetrasInpar = 0
    #Ciclo
    cantVuelt = 0
    sumaLetras = 0
    contPalabra = 0
    ESPACIOFINAL = " ", "."
    #Inicio de programa
    text = input("Ingrese un texto: ")
    text = verificarText(text)
    for car in text:
        if car in ESPACIOFINAL:
            #Punto 3
            vueltaDadaE = False
            #Punto 4
            if contPalabra % 2 == 1:
                sumaLetrasInpar += contPalabra
                palabraImpar += 1
            #ciclo
            contPalabra += 1
            sumaLetras += cantVuelt
            cantVuelt = 0
        else:
            if car in MAYUSC and cantVuelt == 0:
                cantMayus += 1
            if car in NUMBER:
                cantNum += 1
            if car in E and vueltaDadaE:
                cantE += 1
                vueltaDadaE = False
            elif car in E:
                vueltaDadaE = True
            cantVuelt += 1
    print("Cantidad de palabras que empiezan con mayúscula: ", cantMayus)
    print("Cantidad de números del 0 al 9 en todo el texto: ", cantNum)
    print("Cantidad de palabras que tienen más de una e: ", cantE)
    print("Promedio de letras por palabra, para las palabras de longitud impar: ", sumaLetras/contPalabra)
    print("Cantidad de palabras de longitud impar: ", sumaLetrasInpar/palabraImpar)
main()