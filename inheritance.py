class Animal:
    def __init__(self,name,legs,breed):
        self.name=name
        self.legs=legs
        self.breed=breed
        
    def speak(self):
        print("Animal is speak")
        
        
    def show_animal_data(self):
        return f"animal name is {self.name} and animal have {self.legs} legs and animal breed is {self.breed}"
    
class Dog(Animal):
    def __init__(self,name,legs,breed):
        super().__init__(name,legs,breed)
        
        
    def speak(self):
        return ("woofs woofs woofs")
    
    def show_animal_data(self):
        return f"dog name is {self.name} and dog have {self.legs}and dog breed is {self.breed}"
    
    
    
    # animal class object
a1=Animal("dog",4,"german shepared")
print(a1.show_animal_data())
# dog class object
D1=Dog("JACK",4,"pitbuull" )
print(D1.show_animal_data())
print(D1.speak())
