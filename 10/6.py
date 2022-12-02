"""
hola q tal
"""
def buscadorDePalabras(text,x):
    palabrasqueCoinciden = []
    palabra = ''
    for i in text:
        if i in ' .':
            if palabra[0] == x:
                palabrasqueCoinciden.append(palabra)
            palabra = ''
        else:
            palabra += i
    return palabrasqueCoinciden
def verificar(text:str):
    while text[-1] != '.':
        text += '.'
    return text
def main():
    parrafo = verificar(input('usuario porfavor introduzca un parrafo: '))
    letra = input('que letra deseas buscar: ')
    palabrasqueCoinciden = buscadorDePalabras(parrafo,letra)
    for i in palabrasqueCoinciden:
        print(i)
main()
