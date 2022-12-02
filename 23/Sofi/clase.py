class Evento:
    def _init_(self, id, titulo, descripcion, costo, tipo, segmento):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.costo = costo
        self.tipo = tipo
        self.segmento = segmento

    def __str__(self):
        return f'ID: {self.id}, titulo: {self.titulo}, descripcion: {self.descripcion}, costo {self.costo}, tipo {self.tipo}, segmento {self.segmento}'