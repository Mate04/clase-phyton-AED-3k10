def porcentaje(a,b):
    if b != 0: return (a/b)*100
    else: return None
def promedio(a,b):
    if b != 0: return a//b
    else: return None
def verificar():
    text = input('ingrese texto: ').lower()
    if text[-1] != '.':
        text += '.'
    return text
def main():
    text = verificar()
    #punto 1
    banderaDigit = False
    #punto  2
    banderaPunto2 = False
    contPunto2 = 0
    #punto 3
    bandera0 = bandera0Definitiva =False
    antCar = None
    #punto 4
    contAl = sumaLetra4 = 0
    banderaAL = False
    #aux
    contLetras = contPunto1 = contPalabra = 0
    for car in text:
        if car in ' .':
            #punto 1
            if banderaDigit and contLetras >2:
                contPunto1 += 1
            #punto 2
            if banderaPunto2:
                contPunto2 += 1
            #punto 3
            if bandera0:
                bandera0Definitiva = True
            #punto 4
            if banderaAL:
                contAl +=1
                sumaLetra4 += contLetras
            #reiniciador
            contPalabra += 1
            banderaDigit = banderaPunto2=bandera0=banderaAL =False
            contLetras = 0
            antCar = None
        else:
            #punto 1
            if car in '1234567890':
                banderaDigit = True
            #punto 2
            if contLetras == 0 and car == text[0]:
                banderaPunto2 = True
            #punto 3
            if car in 'o':
                bandera0 = True
            #punto 4
            if antCar == 'a' and car == 'l':
                banderaAL = True
            #aux
            antCar = car
            contLetras += 1
    print(f'punto 1: {contPunto1}')
    print(f'punto 2: {porcentaje(contPunto2,contPalabra)}%')
    if bandera0Definitiva: print('existe No hay palabras sin "o"') 
    else: print('Hay palabras sin "o"')
    print(f'punto 4: {promedio(sumaLetra4,contAl)}')
if __name__ == '__main__':
    main()