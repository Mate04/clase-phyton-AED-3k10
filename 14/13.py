def porcentaje(a,b):
    if b != 0: return (a*100)/b
    else: return None
def promedio(a,b):
    if b != 0: return a/b
    else: return None
def verificar():
    text = input('ingrese un texto: ').lower()
    if text[-1] != '.':
        text += '.'
    return text
def main():
    text = verificar()
    #aux
    cont_letra = 0
    for car in text:
        if car in ' .':
            pass
        else:
            cont_letra += 1

if __name__ == '__main__':
    main()