class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def discount(self,amount):
        self.amount=amount
        self.price-=self.amount
        return f" laptop brand : {self.brand}\n new price after discount is : {self.price}"
l1=laptop("hp",10000)
print(l1.discount(2000))