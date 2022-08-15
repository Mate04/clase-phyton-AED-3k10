"""
Determinar el promedio de dígitos por palabra de las palabras formadas solo por dígitos que posee el texto. Por ejemplo, en el texto: “En el 2020 hubo 130 alumnos en el 1k02.” Resultado: 2 palabras cumplen con la condición: (“2020” y “130”) y tienen 7 dígitos  entre la dos. Por lo tanto su promedio de dígitos por palabra es 3.5.
Determinar la cantidad de palabras que finalizan con un dígito y tienen al menos una letra. Por ejemplo, en el texto: “En el 2020 hubo 130 alumnos en el 1k05 y 1k09.” Resultado: 2 palabras cumplen con la condición (“1k05” y “1k09”).
Determinar la longitud y el orden o posición de la palabra más corta del texto. Por ejemplo, para el texto: “Este cuatrimestre hubo 130 alumnos en el 1k02.” Como las palabras más cortas son “en” y “el” de ellas puedo mostrar el orden y la posición de cualquiera de las dos (NO HAY que mostrar la palabra propiamente dicha). Resultado: La longitud es 2 y (si se tomó la primera), la posición es 6.
Determinar la cantidad de palabras que tienen las letras “ch” continuas pero comenzando esa secuencia a partir de la cuarta letra en adelante. Por ejemplo, en el texto: “El chancho cochino juega en la hamaca.” Resultado: 1 palabra cumple con la condición (“chancho”). La palabra "cochino“ no cumple, porque la secuencia "ch" comienza en la tercera letra.
"""

def verificar(text):
    if text[-1] != '.':
        text += '.'
    return text
def main():
    text = input('ingresar un texto: ')
    text = verificar(text)
    #punto 1
    banderaDigito = True
    cantOnlyDig = 0
    #Punto 2
    contPunto2 = 0
    banderaPunto2= banderaPunto24 = False
    contPalabra = 0
    #punto 3
    contLetras = 0
    banderaMenor = True
    #punto 4
    banderaCH = False
    contCH = 0
    for car in text:
        if car in " .":
            #punto 1
            if banderaDigito:
                cantOnlyDig += 1
            #punto 2
            if banderaPunto24:
                contPunto2 += 1
            #punto 3
            if banderaMenor or menorLog > contLetras:
                menorLog = contLetras
                posicionMenor = contPalabra+1
                banderaMenor = False
            if banderaCH:
                contCH += 1
            #aux
            banderaPunto2 = banderaPunto24 = banderaCH= False
            banderaDigito = True
            contLetras = 0
            contPalabra += 1
        else:
            if car not in "1234567890":
                banderaDigito = False
                banderaPunto2 = True
            if banderaPunto2 and car in "1234567890":
                banderaPunto24 = True
            if contLetras > 4 and ultCar in "cC" and car in "hH":
                banderaCH = True
            contLetras += 1
            ultCar = car
    print(f'punto 1: {cantOnlyDig}')
    print(f'punto 2: {contPunto2}')
    print(f'la palabra mas corta fue de longitud {menorLog} y su posicion fue en el {posicionMenor}')
    print(f'punto 4: {contCH}')
main()