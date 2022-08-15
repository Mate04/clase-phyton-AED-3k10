"""
1) Determinar la cantidad de palabras que incluyeron al menos 2 dígitos, por ejemplo, el texto: “Argentina ganó 2 mundiales en 1978 y en 1986.” contiene 2 palabras con al menos 2 dígitos.
2) Determinar la cantidad de palabras que comienzan con “la”, por ejemplo, el texto: “Las laderas de las montañas están labradas.” contiene 4 palabras que comienzan con “la”.
3) Determinar el promedio de letras de las palabras que cumplieron con el punto 2, por ejemplo, en el texto anterior “laderas” y “labradas” cumplieron la condición y su promedio de letras por palabra fue 7.5.
4) Determinar la cantidad de palabras que comenzaron con “ll” y además incluyeron alguna “v”. Por ejemplo, en el texto: “Las lluvias se llevaron los llantos.”, contiene 2 palabras que cumplen la condición.
"""
def verificarText(text):
    while text[-1] != '.':
        text += '.'
    return text

def main():
    text = input("Ingrese un texto: ")
    text = verificarText(text)
    #Punto 1
    digitos = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    cantDigitos = 0
    banderaDigitos = False
    auxDigito = 0
    #punto 2
    L = "l", "L"
    A = "a", "A"
    cantLA = 0
    #Punto 3
    sumaLetrasPunto2 = 0
    PromedioBandera = False
    #Punto 4
    L = "l", "L"
    V = "v", "V"
    contLV = 0
    banderaV = False
    #ciclos
    FIN = " ", "."
    contVuelta = 0
    for car in text:
        if car in FIN:
            #punto 1
            banderaDigitos = False
            auxDigito = 0
            #punto 3
            if PromedioBandera:
                sumaLetrasPunto2 += contVuelta
                PromedioBandera = False
            #punto 4
            banderaV = False
            #auxiliar
            contVuelta = 0
            ultCar = None
        else:
            #punto 1
            if car in digitos and banderaDigitos and auxDigito == 0:
                cantDigitos += 1
                banderaDigitos = False
                auxDigito = 1
            elif car in digitos:
                banderaDigitos = True
            #Punto 2
            if car in A and ultCar in L and contVuelta == 1:
                cantLA += 1
                #Punto 3
                PromedioBandera = True
            #Punto 4
            if car in L and contVuelta == 1 and ultCar in L:
                banderaV = True
            elif car in V and banderaV:
                contLV += 1
                banderaV = False
            #aux
            ultCar = car
            contVuelta += 1
    print("Cantidad de palabras que incluyeron al menos 2 dígitos: ", cantDigitos)
    print("Cantidad de palabras que comienzan con “la”: ", cantLA)
    print("Promedio de letras de las palabras que cumplieron con el punto 2: ", sumaLetrasPunto2/cantLA)
    print("Cantidad de palabras que comenzaron con “ll” y además incluyeron alguna “v”: ", contLV)
main()