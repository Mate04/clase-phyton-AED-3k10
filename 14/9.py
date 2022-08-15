def porcentaje(a,b):
    if b != 0: return (a*100)/b
    else: return None
def verificar():
    text = input('ingrese un text: ')
    if text[-1] != '.':
        text += '.'
    text = text.lower()
    return text
def main():
    text = verificar()
    contLetra = 0
    contPalabra = 0
    #punto 1
    banderaMO = False
    contMO = 0
    #punto 2
    contDigit = contPalabraDigit = 0
    #punto 3
    banderaPunto3 = False
    contPunto3= 0
    for car in text:
        if car in ' .':
            if banderaMO:
                contMO += 1
            #punto 2
            if contDigit >= 2:
                contPalabraDigit += 1
            if banderaPunto3:
                contPunto3 += 1
            #reinicio
            contPalabra += 1
            banderaMO = banderaPunto3 = False
            contLetra = contDigit = 0
        else:
            #punto 1
            if car in 'mo' and contLetra>= 1:
                banderaMO = True
            #punto 2
            if car in '1234567890':
                contDigit += 1
            #punto 3
            if car in 'aeiou' and (contLetra+1)%2 == 0:
                banderaPunto3 = True
            #TODO:aux
            contLetra+=1
    print(f'punto 1: {contMO}')
    print(f'punto 2: {porcentaje(contPalabraDigit,contPalabra)}')
    print(f'punto 3: {contPunto3}')
main()