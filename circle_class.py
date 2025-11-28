import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def circumference_of_circle(self):
        circumference=2 * math.pi * self.radius
        return circumference

cir=Circle(50)
print("circumference of ciricle is : ",cir.circumference_of_circle())