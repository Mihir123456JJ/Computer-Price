class Computer:
    def __init__(self):
        self.__maxprice=19000
    def display(self):
        print("Selling price is",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
person1=Computer()
person1.display()
person1.__maxprice=20000
person1.display()
person1.setmaxprice(23000)
person1.display()        

            
            
