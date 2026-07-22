class Vehicle:
    def __init__(self, model, wheelsize, brand):
        self.model=model
        self.wheelsize=wheelsize
        self.brand=brand
    def showdetails(self):
        print(self.brand, "has launched a new model called", self.model, "which has a wheel size of", self.wheelsize) 
class Car(Vehicle):
    def __init__(self, model, wheelsize, brand):
        super().__init__(model, wheelsize, brand)

    def yearitwasmade(self,year):
        print("This car was made in", year)
        
    
    def showdetails(self):
        super().showdetails()
ob1=Car("Leaf", 235, "Nissan")
ob1.showdetails()
ob1.yearitwasmade(2023)

print("Is Car a sublcass of Vehicle?", issubclass(Car,Vehicle))

