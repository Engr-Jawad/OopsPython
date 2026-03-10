class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def deatils_of_car(self):
        return f"make : {self.make}\nmodel : {self.model}\nyear : {self.year}"
    
c1=car("toyota","carolla",2020)
print(c1.deatils_of_car())