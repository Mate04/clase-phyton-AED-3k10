"""
Determinar cuántas palabras tenían por lo menos tres vocales y más de cuatro letras. Por ejemplo, en el texto: “La universidad es una etapa más de la vida.”, hay dos palabras que cumplen la condición ("universidad" y "etapa").
"""

def verificarText(text):
    while text[-1] != '.':
        text += '.'
    return text

def main():
    text = input('ingresar texto: ')
    text = verificarText(text)
    #punto 1
    letras = 0
    vocales = 'aeiouAEIOU'
    contVocales = 0
    masde4letras = 0
    #punto 2 
    digitos = '1234567890'
    segundoPunto = False
    bandera2doPunto = True
    #punto 3
    comienzoVP = 'vVpP'
    ultimoLetra = 'nNaA'
    banderaVP = False
    contadorPunto3 = 0
    #aux
    cortador = ' ', '.'
    for car in text:
        if car in cortador:
            if letras > 4 and contVocales > 3:
                masde4letras += 1
            #punto 2
            if segundoPunto:
                if bandera2doPunto or palabraCorto > letras:
                    palabraCorto = letras
                    bandera2doPunto = False
                    segundoPunto = False
            #punto 3
            if banderaVP and ultimaCar in ultimoLetra:
                contadorPunto3 += 1
            #aux
            letras = 0
        else:
            if car in vocales:
                contVocales += 1
            if car not in vocales and car not in digitos and car and letras == 1:
                segundoPunto = True
            if car in comienzoVP:
                banderaVP = True
            ultimaCar = car
            letras += 1
    print(f'palabras con mas de 4 letras y 3 vocales {masde4letras}')
    print(f'la palabra mas corta fue de {palabraCorto}')
    print(f'la palabras q empieza con v,p y termina n,a son {contadorPunto3}')
main()