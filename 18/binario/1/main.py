import os

fb = f'{os.path.dirname(os.path.realpath(__file__))}/frases.dat'


def crear(fb):
    with open(fb, 'wb') as f:
        f.write(b'Phyton es tremendo')
        f.write(b'\n')
        f.write(b'Resto del archvio')
        f.write(b'\n')
        f.write(b'Fin del archivo')
    f.close()
def leer(fb):
    with open(fb,'rb') as f:
        datos = f.read()
        print(datos.decode('utf-8'))
    f.close()
crear(fb)
leer(fb)