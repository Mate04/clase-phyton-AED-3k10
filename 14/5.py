def porcentaje(a,b):
    if b != 0:
        return (a/b)*100
    else:
        return None
def promedio(a,b):
    return a/b
def verificar(text):
    if text[-1] != '.':
        text += '.'
    text = text.lower()
    return text
def main():
    text = input('ingrese texto: ')
    text = verificar(text)
    #punto 1
    contVocales = contDig = contConsonante = 0
    contLetraTotales = 0
    #punto 2
    contCosonanteXpalabra = contVocalesXpalabra = contPunto2 = sumPunto2 = 0
    #punto 3
    contPunto3 = 0
    banderaPunto3 =banderaCapicua = False
    #punto 4
    banderaLL = banderaS = False
    #aux
    contLetra = contPunto4 = vuelta =0
    for car in text:
        if car in " ,.":
            #TODO:punto 2
            if contVocalesXpalabra > contCosonanteXpalabra:
                sumPunto2 += contLetra
                contPunto2 += 1
            #TODO: punto 3
            UltCarAnterio = ultCar
            if banderaCapicua and 50 < porcentaje(posicion,contLetra):
                contPunto3 += 1
            banderaCapicua = False
            #TODO: punto 4
            if banderaLL and banderaS:
                contPunto4 += 1
            banderaS = banderaLL = False
            #aux
            contLetra = contVocalesXpalabra = contCosonanteXpalabra = 0
            banderaPunto3 = True
        else:
            #TODO:punto 1
            if car in 'aeiou':
                contVocales += 1
                contVocalesXpalabra += 1
            elif car in '1234567890':
                contDig += 1
            else:
                contConsonante += 1
                contCosonanteXpalabra += 1
            contLetraTotales += 1
            #TODO: punto 3 
            if banderaPunto3 and UltCarAnterio == car:
                posicion = contLetra+1
                banderaCapicua = True
            #TODO: punto 4
            if vuelta > 0 and ultCar in "lL" and car in "lL":
                banderaLL = True
            if car in 'sS':
                banderaS = True
            #!aux
            vuelta = 1
            ultCar = car
            contLetra += 1
            
    print(f'porcentaje de vocales {porcentaje(contVocales,contLetraTotales)}%\nPorcentaje de consonantes {porcentaje(contConsonante,contLetraTotales)}%\nPorcentaje de Digitos {porcentaje(contDig,contLetraTotales)}%')
    if contPunto2 >0:
        print(f'el promedio de letras de palabras q contiene mas vocales que consonante son: {promedio(sumPunto2,contPunto2)}')
    print(f'punto 3: {contPunto3}')
    print(f'punto 4: {contPunto4}')
main()