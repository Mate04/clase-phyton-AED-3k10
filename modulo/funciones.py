import colores

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b != 0:
        return a/b
    else:
        return colores.RED+'No se puede dividir entre 0'+colores.WHITE
def porcentaje(a,b):
    if a != 0:
        return f'{(a/b)*100}%'
    else:
        None
def promedio(a,b):
    if b != 0:
        return a/b
    else:
        return colores.RED+'No se puede dividir entre 0'+colores.WHITE
def verificador(num:int,a:int,b:int):
    if a == b:
        while num <= 0:
            num = int(input(colores.RED+'ingrese una cantidad valida: '+colores.WHITE))
        return num
    else:
        while num < a or num > b:
            num = int(input(colores.RED+f'ingrese un numero entre {a} y {b}: '+colores.WHITE))
    return num
def mcd(a:int,b:int):
    if a > b:
        while b != 0:
            r = a%b
            a = b
            b = r
        return a
    else:
        return colores.RED+'no se puede encontar el maximo comun multiplo ya que A es menor que B'+colores.WHITE