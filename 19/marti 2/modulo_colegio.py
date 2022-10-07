
class Profesionales():
    def __init__(self,dni,nombre,importe,tipo,trabajo):
        self.dni=dni
        self.nombre=nombre
        self.importe=importe
        self.tipo=tipo
        self.trabajo=trabajo
    def __str__(self):
        return "DNI:"+str(self.dni)+" -Nombre :" +str(self.nombre)+ "Importe:" +str(self.importe)+"-Tipo:"+str(self.tipo)+"-trabajo:"+str(self.trabajo)
def add_in_order(vec,profe):
    n=len(vec)
    izq=0
    der=n-1
    pos=n
    while izq<=der:
        c=(der+izq)//2
        if vec[c].dni==profe.dni:
            pos=c
            break
        if profe.dni<vec[c].dni:
            der-=1
        else:
            izq+=1
    if izq>der:
            pos=izq
    vec[pos:pos]=[profe]


