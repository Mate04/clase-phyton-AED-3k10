import os

class qsy:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __str__(self) -> str:
        return f'a: {self.a}, b: {self.b}'
listado = [qsy(4,5),qsy(4,5)]
archivoTxt = f'{os.path.dirname(os.path.realpath(__file__))}/pruea.txt'
archivo = open(archivoTxt,'w')
for i in listado:
    archivo.write(str(i)+'\n')
archivo.close()