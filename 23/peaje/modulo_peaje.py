class Peaje:
    def __init__(self,num_i,nom,monto,patente,hora):
        self.num_i=num_i
        self.nom=nom
        self.monto=monto
        self.patente=patente
        self.hora=hora
def to_str(elemento):
    res=" "
    res+="|Numero de id:"+str(elemento.num_i)
    res+="|Nombre:"+str(elemento.nom)
    res+="|Monto:"+str(elemento.monto)
    res+="|Patente:"+str(elemento.patente)
    res+="|Hora:"+str(elemento.hora)
    return res

