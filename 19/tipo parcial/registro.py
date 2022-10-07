class Registro:
    def __init__(self,id:int,descripcion:str,precio:int,lugar:int,articulo:int):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.lugar = lugar
        self.articulo = articulo
    def __str__(self) -> str:
        return f'id: {self.id}, descripcion: {self.descripcion}, precio: ${self.precio}, lugar: {self.lugar}'
