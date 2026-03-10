from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class squre(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        are = self.length * self.width
        return are
    
class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        aree=0.5*self.base * self.height
        return aree
s1=squre(5,10)
print("area of a squre : ",s1.area())
t1=triangle(5,10)
print("area of the triaangle : ",t1.area())
        
    