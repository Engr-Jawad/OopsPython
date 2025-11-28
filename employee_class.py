class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def give_raise(self,amount):
        self.amount=amount
        self.salary+=amount
        return f"new salary for {self.name} :{self.salary}"
    
e1=employee("jawad ali",5000)
print(e1.give_raise(2000))