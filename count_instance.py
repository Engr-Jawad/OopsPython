class person:
    count=0
    def __init__(self,name,age,address):
        count=0
        count+=1
        self.name=name
        self.age=age
        self.address=address
        person.count+=1
        
    def show_person(self):
        return f"person name {self.name}\nperson age: {self.age}\nperson address : {self.address}"
    

p1=person("jawad ali",23,"kalpani")
print(p1.show_person())
p1=person("waqas ali",45,"bajkata")

print("number of object created:",person.count)