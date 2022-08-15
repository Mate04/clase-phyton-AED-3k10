"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:
1 - Determinar la cantidad de palabras que tienen dos o más vocales (minúsculas o mayúsculas) y que no contienen ni "q" ni "z"  (minúsculas o mayúsculas). Por ejemplo, en el texto: "Los cursos se evalúan con quiz." hay 2 palabras que cumplen con la condición: "cursos" y "evalúan". 
2 - Determinar la cantidad de palabras que tienen la segunda letra (minúscula o mayúscula) igual que su última letra (minúscula o mayúscula). Por ejemplo, en el texto: "Hola casa azul." hay 1 palabra ("casa") que cumple con la condición.
3 - Determinar cuántas palabras de longitud mayor a dos, empiezan con el segundo caracter de la primera palabra del texto (en minúscula o en mayúscula). Por ejemplo, en el texto: "Para el alfil no hay alcance." hay dos palabras ("alfil" y "alcance") que cumplen con la condición.
4 - Determinar la cantidad de palabras que contienen la expresión "pa" o "pA" (la "p" en minúscula) pero de forma que la palabra no termine con esa expresión. Por ejemplo en el texto: "Se paran y se sacan la capA para no tener frío en casa de Pablo.“, hay 2 palabras que cumplen con la condición: "paran" y "para". La palabra "Pablo" no cuenta porque la "P" está en mayúscula, y la palabra "capA" tiene la secuencia pedida, pero no cuenta porque la palabra termina ella.
"""
def verificar():
    text = input('ingresar texto: ')
    if text[-1]!= '.':
        text += '.'
    return text
def main():
    text = verificar()
    #punto 1
    contVocales = contQZ = 0
    banderaQZ = False
    #punto 2
    contPunto2 = 0
    #punto 3
    banderaInicial = True
    contPunto3 = 0
    #punto 4
    banderaPA = False
    contPunto4 = 0
    #aux
    contLetra = contPalabra =0
    for car in text:
        if car in ' .':
            #punto 1
            if banderaQZ == False and contVocales >= 2:
                contQZ += 1
            #punto 2
            if segundaLetra == ultCar:
                contPunto2 += 1
            #punto 3
            if primeraLetraPalabra == segundaLetraDelTexto:
                contPunto3 += 1
            #punto 4
            if banderaPA and posicion != contLetra:
                contPunto4 += 1
            #reincio
            contVocales = contLetra =0
            banderaQZ = banderaPA =False
            segundaLetra = ultCar =primeraLetraPalabra= None
            contPalabra += 1
        else:
            #punto 1
            if car in 'qzQZ':
                banderaQZ = True
            if car in 'aeiouAEIOU':
                contVocales += 1
            #punto 2
            if contLetra == 1:
                segundaLetra =  car 
            #punto 3
            if contLetra == 1 and banderaInicial:
                segundaLetraDelTexto = car
                banderaInicial = False
            elif contLetra == 0:
                primeraLetraPalabra = car
            #punto 4
            if contLetra >0 and ultCar in "p" and car in "aA":
                banderaPA= True
                posicion = contLetra+1
            #aux
            ultCar = car
            contLetra += 1
    print(f'punto 1: {contQZ}')
    print(f'punto 2: {contPunto2}')
    print(f'punto 3: {contPunto3}')
    print(f'punto 4: {contPunto4}')
if __name__ == '__main__':
    main()