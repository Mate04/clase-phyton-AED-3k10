class mascotas:
    def __init__(self, name, raza):
        self.__name = name
        self.raza = raza
    def getDetail(self):
        return 'esta mascota se llama '+ self.__name + ' y es un '+ self.raza

katara = mascotas('katara', 'gato')
print(katara.getDetail())