class animal:
    def __init__(self,name):
        self.name=name
    def generic_sound(self,sound):
        self.sound=sound
        generic_soun=self.sound
        return f" animal name is {self.name} generic sound of the animal is : {generic_soun}"
a1=animal("cat")
print(a1.generic_sound("meo meo"))
a2=animal("dog")
print(a2.generic_sound("gwhap gwhap"))
