class Drink:
    count = 0
    def __init__(self, name, price):
        self.__name = name
        self.price = price
        Drink.count += 1
    def getDetails(self):
        return "La bebida es "+self.__name + " y su precio es de " + str(self.price)
    @staticmethod
    def getCount():
        return Beer.count

class Beer(Drink):

    

    def __init__(self, name, price,alcohol):
        super().__init__(name, price)
        self.alcohol = alcohol
    def getDetails(self):
        return super().getDetails() + " y es una bebida " + self.alcohol
    
beer1 = Beer("Pilsen", 5, "Alcoholica")
print(beer1.getDetails())
print(Drink.getCount())