def verificarTexto(text):
    while text[-1] != '.':
        text += "."
    return text

def main():
    #Punto 1
    MB = "m","M","b","B"
    contMB = 0
    banderaMB = True
    #punto 2
    P = "P","p"
    vocales = "a","e","i","o","u"
    banderaP = False
    cont_P_mas_Vocal = 0
    #punto 3
    cont_Capicua = 0
    #Variables auxiliares
    cont = 0
    text = input('Ingresa un texto que contenga un punto al final: \n')
    textVerificado = verificarTexto(text)
    for car in textVerificado:
        if car == " " or car == '.':
            if auxPrimeraVocal == auxUltimaVocalUsada:
                cont_Capicua += 1
            cont = 0
            banderaMB = False
        else:
            #Punto 1
            if car in MB and cont >= 2:
                banderaMB == True
            if car in MB and cont < 2 and banderaMB == True:
                contMB += 1
            #Punto 2
            if car in P and cont == 0:
                banderaP = True
            elif car in vocales and banderaP == True:
                cont_P_mas_Vocal += 1
                banderaP = False
            elif car not in vocales and banderaP == True:
                banderaP = False
            #Punto 3
            if cont == 0:
                auxPrimeraVocal = car
            auxUltimaVocalUsada = car
            #Contador
            cont += 1
    print(f'Punto 1: {contMB}')
    print(f'punto 2: {cont_P_mas_Vocal}')
    print(f'punto 3: {cont_Capicua}')
main()