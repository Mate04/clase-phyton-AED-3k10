def verificarText(text):
    while text[-1] != '.':
        text += '.'
    text = text.lower()
    return text
text = input('ingrese text: ')
text = verificarText(text)
#punto 1
contLetras = 0
contPalabraMay4 = 0
#punto 2
contXY = 0
xy = 'xy'
banderaXY = True
#punto 3
contLetrasText = 0
contPalabras = 0
#punto 4
M = 'm'
O = 'o'
banderaMO = False
contMO = 0
anterior = None
vueltas = 0
#aux
cortador = " ", '.'
for car in text:
    if car in cortador:
        if contLetras > 4:
            contPalabraMay4 += 1
        if banderaXY:
            contXY += 1
            banderaXY = False
        if banderaMO:
            contMO += 1
            banderaMO = False
        anterior = None
        contPalabras += 1
        contLetras = 0
        vueltas = 0
    else:
        #punto 1
        contLetras += 1
        #punto 2
        if car in xy:
            banderaXY = True
        #punto 3
        contLetrasText += 1
        #punto 4
        #paso 2
        if vueltas >= 1 and anterior in M and car in O:
            banderaMO = True
        #paso 1
        anterior = car
        vueltas += 1
print(f'punto 1: {contPalabraMay4}')
print(f'punto 2: {contXY}')
print(f'punto 3: {contLetrasText//contPalabras}')
print(f'punto 4: {contMO}')
