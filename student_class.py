class student:
    # this is a class attribute and store for all object in the same memory
    college_name="gdc buner"
    # the below function is a parametarized constructor
    # the self refrenced parameter which pointing the current object
    def __init__(self,name,marks,rollno,address):
        # the below is the object atrribute and the attribute store in the diffrent memory in the 
        self.name=name
        self.marks=marks
        self.rollno=rollno
        self.address=address
        # the function in the class is called method or member function
    def show_student_data(self):
        return f"student name : {self.name} student marks : {self.marks} student rollno : {self.rollno} student address : {self.address}"
    # get marks method
    def get_marks(self):
        return self.marks
        
        
class std:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_average(self):
        sum=0
        for  value in self.marks:
            sum+=value
        print("your averge score is equal to : ",sum/3)
        
ss=std("jawad ali",[89,98,99])
print(ss.get_average())
            
       
s1=student("jawad ali",56,34,"kalpani")  #the paranthesis after the student is calling the init function or calling the constructor
print(s1.get_marks())
print(s1.show_student_data())

