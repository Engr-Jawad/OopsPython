class student:
    total_marks=1100
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def average(self):
        return self.marks % self.total_marks
        
s1=student("jawad ali",980)
print(s1.average())