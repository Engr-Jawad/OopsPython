"""
we have four pillar of object oriented programming the fist one is Abstraction and the abstraction mean showing only those deatalis which are essential and hide unecssary details 
                                      OR
TO show only those details  which are important for the current perspective and it is also called information hiding its mean to hide data from the outside world 
"""
class Car:
    def __init__(self):
        # hide the unncessary details like acc,brk,cltch
        # its all insude the class
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start(self):
        self.acc=True
        self.clutch=True
        self.brk=True
        print("car is start")

c=Car()
c.start()