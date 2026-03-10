class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_data(self):
        return f"person name : {self.name}\nperson age : {self.age}"
p1=Person("jawad ali",20)
print(p1.show_data())