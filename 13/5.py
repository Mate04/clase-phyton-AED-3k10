def ASCII(car):
    return ord(car)
def verificarText(text):
    while text[-1] != '.':
        text += '.'
    return text
def main():
    text = input('Ingresa un texto: ')
    text = verificarText(text)
    #Punto 1 
    vocal = 'a', 'e', 'i', 'o', 'u'
    endVocal = 0
    #punto 2
    consonantes = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    contConsonantes = 0
    contVocal = 0
    contLetras = 0
    #punto 3
    contadorDeOrden = 1
    banderaMay = True
    contConstanteEnCiclo = 0
    #Punto 4
    banderaPrimerLetraText = True
    S = 's', 'S'
    T = 't', 'T'
    contSt = 0
    #fin del ciclo
    contLetrasEnElCiclo = 0
    fin = ' ', '.'
    ultCar = None
    for car in text:
        if car in fin:
            #punto 1
            if ultCar in vocal:
                endVocal += 1
            #punto 2
            contLetras += contLetrasEnElCiclo
            #punto 3
            if banderaMay or contMayConst < contConstanteEnCiclo:
                contMayConst = contConstanteEnCiclo
                contOrdenMay = contadorDeOrden
                banderaMay = False
            #fin del ciclo
            contadorDeOrden +=1
            contLetrasEnElCiclo = 0
            contConstanteEnCiclo = 0
            ultCar = None
        else:
            if car in vocal:
                contVocal += 1
            if car in consonantes:
                contConsonantes += 1                
                #punto 3
                contConstanteEnCiclo += 1
            #punto 4
            if banderaPrimerLetraText:
                primerCarText = car
                DexPrimeraCarText = ASCII(primerCarText)
                banderaPrimerLetraText = False
            elif contLetrasEnElCiclo == 0:
                PrimeraCaracterDelCiclo = car
                DexPrimeraCaracterDelCiclo = ASCII(PrimeraCaracterDelCiclo)
            if ultCar in S and car in T:
                if DexPrimeraCaracterDelCiclo == DexPrimeraCarText or DexPrimeraCaracterDelCiclo == DexPrimeraCarText-32 or DexPrimeraCaracterDelCiclo == DexPrimeraCarText+32:
                    contSt += 1
            ultCar = car
            contLetrasEnElCiclo += 1
    print('El texto tiene', endVocal, 'vocal(es) al final')
    print('El texto tiene', contVocal, 'vocal(es)')
    print('El texto tiene', contConsonantes, 'consonante(s)')
    print('El texto tiene', contLetras, 'letra(s)')
    print('La mayor cantidad de constantes en una palabra es', contMayConst, 'en la palabra orden', contOrdenMay)
    print('El texto tiene', contSt, '"st" y su primera letra', primerCarText, 'cumple con los textos')
main()