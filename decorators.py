""" ist the static method is called decorators and decorators are those function which are on the class level not on the object level or decorators are those functions or methods which donot take a self parameter and it take functions as a parameter and output of the decorators is also a function
"decorators alllows us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it"

"""

class student:
    # static method
    @staticmethod  # decorators
    def welcome():
        print("welcome to the college")
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