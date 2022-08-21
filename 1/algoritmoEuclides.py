
a = int(input('ingrese A'))
b = int(input('ingrese B'))
if a > b:
    while b != 0:
        r = a%b
        a = b
        b = r
    print(a)
else:
    print('no se puede encontar el maximo comun multiplo ya que A es menor que B')