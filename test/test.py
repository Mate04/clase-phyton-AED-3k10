class Nombre:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return self.nombre
    def getData(self):
        return self.nombre
def main():
    arrayqsy = []
    for i in range(2):
        nombre = input('nombre: ')
        print(Nombre(nombre).getData())
        arrayqsy.append(Nombre(nombre).getData())
    print(arrayqsy)
if __name__ == '__main__':
    main()