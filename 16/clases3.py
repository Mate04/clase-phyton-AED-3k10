class personaje:
    def __init__(self, name:str, age:int, sexo:str,power:str,healt:int):
        self.name = name
        self.age = age
        self.sexo = sexo
        self.power = power
        self.healt = healt
    def getDetails(self):
        return f'El nombre del jugador es {self.name}\nsu edad es {self.age}\nsu sexo es {self.sexo}\nsu poder es {self.power}\nsu salud es {self.healt}'
#inicializacion
player1= personaje('Mateo',20,'masculino','fuego',122)
print(player1.getDetails())