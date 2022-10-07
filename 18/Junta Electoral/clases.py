class Voto:
    def __init__(self,candidato:int,provincia:int,votante:str) -> None:
        self.candidato = candidato
        self.provincia = provincia
        self.votante = votante
    def __str__(self) -> str:
        return f'candidato numero {self.candidato}, numero de provincia: {self.provincia}, votante: {self.votante}'
    def getData(self):
        return [self.candidato, self.provincia,self.votante]
class Candidato:
    def __init__(self,codigo,nombre) -> None:
        self.codigo = codigo
        self.nombre = nombre
    def getData(self):
        return [self.codigo,self.nombre]