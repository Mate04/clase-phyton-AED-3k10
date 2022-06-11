"""
Se solicita procesar un texto caracter a caracter. Las palabras del texto se separan con espacios en blanco y el fin del texto se indica con un punto.

A partir del texto se pide:
a. Determinar la cantidad de palabras que comienzan con la expresión ´SI´.
b. Determinar la cantidad de palabras que terminan con vocal y tienen una cantidad impar de letras.
c. Determinar la cantidad de palabras que tienen sólo una vocal.
d. Determinar la cantidad de palabras que comienzan y terminan con la misma letra.
e. Determinar la cantidad de palabras que contienen la expresión ´CC´.
f.  Determinar el porcentaje que representan las palabras del punto b sobre el total de palabras.
g. Determinar la longitud de la palabra más corta.
h. Determinar el promedio de letras por palabra.
"""
def verificarText(text):
    while text[-1] != '.':
        #agregarle un punto final al text
        text += '.'
    return text
def main():
    text = input("Ingrese un texto: ")
    #verificar que el texto no termine con un punto
    text = verificarText(text)
    contVueltas = 0
    contDePalabras = 0
    #Punto A
    S = "s", "S"
    I = "i", "I"
    contDePalabrasSI = 0
    #Punto B
    vocal = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    contDePalabrasInparVocal = 0
    #Punto C
    contLetrasVocal = 0
    contDe1Vocal = 0
    #Punto D
    contDeCapicua = 0
    #Punto E
    C = "c", "C"
    contDeCC = 0
    banderaC = False
    #Punto G
    banderaCorta = True
    #Punto H
    contDeLetras = 0
    final = " ","."
    for car in text:
        if car in final:
            #TODO: si es impar
            if contVueltas % 2 != 0:
                #Punto B
                if endCaracter in vocal:
                    contDePalabrasInparVocal += 1
            else:
                pass
            #Punto C
            if contLetrasVocal == 1:
                contDe1Vocal += 1
                contLetrasVocal = 0
            else:
                contLetrasVocal = 0
            #PUNTO D
            if primeraCar == endCaracter:
                contDeCapicua += 1
            #Punto E
            banderaC = False
            #Punto G
            #determinar la palabra mas corta
            if banderaCorta or contVueltas < palabraMasCorta:
                palabraMasCorta = contVueltas
                banderaCorta = False
            #Punto H
            contDeLetras += contVueltas
            #Ultimo Ciclo
            contVueltas = 0
            contDePalabras +=1
        else:
            if contVueltas == 0:
                primeraCar = car
            #Punto A
            elif contVueltas == 1 and car in I and primeraCar in S:
                contDePalabrasSI +=1
            #Punto C
            if car in vocal:
                contLetrasVocal += 1
            #Punto E
            if car in C and banderaC:
                contDeCC += 1
                banderaC = False
            elif car in C:
                banderaC = True
            else:
                banderaC = False
            endCaracter = car
            contVueltas += 1
    print("Punto A: ", contDePalabrasSI)
    print("Punto B: ", contDePalabrasInparVocal)
    print("Punto C: ", contDe1Vocal)
    print("Punto D: ", contDeCapicua)
    print("Punto E: ", contDeCC)
    print("Punto F: ", (contDePalabrasInparVocal/contDePalabras)*100,"%")
    print("Punto G: ", palabraMasCorta)
    print("Punto H: ", (contDeLetras//contDePalabras))

main()