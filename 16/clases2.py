class Auto:
    def __init__(self, name,price):
        self.name = name
        self.price = price
    def getDetails(self):
        return "El nombre del auto es "+self.name+" y su precio es de: "+ str(self.price)+ "."
class AutoSpecial(Auto):
    def __init__(self,name,price,type):
        super().__init__(name,price)
        self.type = type
    def getDetails(self):
        return super().getDetails() + 'y es de tipo ' + self.type
Tesla = AutoSpecial('tesla',1000,'electrico')
print(Tesla.getDetails())