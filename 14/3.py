"""
3) Determinar cuántas palabras contienen (pero sin empezar con él) al último caracter de la primera palabra del texto (en minúscula o en mayúscula). Por ejemplo, en el texto: "Bienvenidos son los alumnos." la primera palabra finaliza con 's' y hay entonces 2 palabras que contienen a esa letra sin comenzar con ella ("los" y "alumnos"). La palabra "son" contiene una "s", pero comienza con ella, y por lo tanto no debe ser contada.
"""
def verficar(text):
    if text[-1] != '.':
        text += '.'
    return text
def main():
    text = input('ingresar text: ')
    text = verficar(text)
    #punto 3
    ultimaLetra1raPalabra = True
    contPunto3 = 0
    #aux
    reiniciador = " ."
    for car in text:
        if car in reiniciador:
            if ultimaLetra1raPalabra:
                ultCar1raPalabra = ultCar
                ultimaLetra1raPalabra = False
            elif ultCar1raPalabra == ultCar:
                contPunto3 += 1
        else:
            ultCar = car
    print(f'punto 3: {contPunto3}')
main()