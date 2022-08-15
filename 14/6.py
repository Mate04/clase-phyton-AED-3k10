def verficar(text):
    if text[-1] != '.':
        text += '.'
    text = text.lower()
    return text
#123
def main():
    text = input('ingrese un texto ')
    text = verficar(text)
    #punto2
    contador45 = 0
    for caracter in text:
        if caracter in ' .':
            if ultCar in '45':
                contador45 += 1
        else:
            ultCar = caracter
    print(f'contador de ultimos digitos en 4 o 5 son: {contador45}')
if __name__ == '__main__':
    main()