# inheritance mean when a class derives from another class its sometthing like we also study in biology  when a child inherits som charctersitics from parents
# in inheritance we have tow main classes ths ist one is base class or parent class and the other is derived class or child class
# the child class inherits the properties and menthods of the parent class
class Car:
    @staticmethod
    def car_start():
        print("car startd ...")
    @staticmethod
    def car_Stop():
        print("car stopped ...")
class toyota(Car):
    def __init__(self,name,color,type,model):
        self.name=name
        self.color=color
        self.type=type
        self.model=model
    def car_details(self):
        print(f"cane name : {self.name}\ncar color : {self.color}\ncar type : {self.type}\ncar model : {self.model}")


car1=toyota("lexus","black","petrol",2026)
car1.car_start()
car1.car_details()
car1.car_Stop()