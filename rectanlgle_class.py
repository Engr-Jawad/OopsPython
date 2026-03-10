class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_of_rectagle(self):
        area=self.length * self.width
        return area
    def perameter_of_rectagle(self):
        return 2 * (self.length + self.width)
    
r1=Rectangle(10,20)
print("area of rectagle is : ",r1.area_of_rectagle())
print("perameter of rectagle is  : ",r1.perameter_of_rectagle())