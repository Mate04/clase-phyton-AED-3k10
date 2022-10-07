class Registro:
    def __init__(self,dni:int,nombre:str,importe:int,afilacion:int,id:int):
        self.dni = dni
        self.nombre = nombre 
        self.importe = importe
        self.afilacion = afilacion
        self.id = id
    def __str__(self) -> str:
        return f'DNI: {self.dni}, nombre {self.nombre}, importe: {self.importe}, afilacion {self.afilacion}, ID: {self.id}'
