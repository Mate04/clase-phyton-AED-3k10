def porcentaje(a,b):
    if b > 0:
        return (a/b)*100
    else:
        return None
def verificar():
    text = input('ingrese texto: ')
    if text[-1] != '.':
        text += '.'
    text = text.lower()
    return text
def main():
    for car in verificar():
        if car in ' .':
            pass
        else:
            print(car)
if __name__ == '__main__':
    main()