
def porcentaje(a,b):
    if b != 0: return (a/b)*100
    else: return None
def promedio(a,b):
    if b != 0: return a/b
    else: return None
def verificar():
    text = input('ingrese un texto: ')
    if text[-1]!= '.':
        text += '.'
    return text
def main():
    text = verificar()
    #punto 1
    contVocales = punto1 =0
    banderaQZ = False
    #punto 2
    segundaPositions = None
    contPunto2 = 0
    #punto 3
    banderaPunto3 = False
    contPunto3 = 0
    #punto 4
    banderaPA = False
    position = None
    contPunto4 = 0
    #aux
    contLetra = 0
    ultCar = None
    for car in text:
        if car in ' .':
            #punto 1
            if banderaQZ== False and contVocales >= 2:
                punto1+= 1
            #punto 2
            if segundaPositions == ultCar:
                contPunto2 += 1
            #punto 3
            if banderaPunto3:
                contPunto3 += 1
            #punto 4
            if banderaPA and position < contLetra:
                contPunto4 += 1
            #reiniciador
            contVocales = contLetra = 0
            banderaQZ =banderaPunto3= banderaPA =False
            ultCar = position = None
        else:
            #punto 1
            if car in 'aeiou':
                contVocales += 1
            if car in 'qQzZ':
                banderaQZ = True
            #punto 2
            if contLetra == 1:
                segundaPositions = car
            #punto 3
            if contLetra == 0 and car == text[1]:
                banderaPunto3 = True
            #punto 4
            if ultCar == 'p' and car in 'aA':
                position = contLetra+1
                banderaPA =True
            #aux
            ultCar = car
            contLetra += 1
    print(f'punto 1: {punto1}')
    print(f'punto 2: {contPunto2}')
    print(f'punto 3: {contPunto3}')
    print(f'punto 4: {contPunto4}')
if __name__ == '__main__':
    main()