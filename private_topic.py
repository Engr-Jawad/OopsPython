class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_(self,new_pass):
            self.__acc_pass=new_pass
            new_pass=input("enter your new password :")
            print("your  password has been changed successfully ")
    def display(self):
                print("account numbner :",self.acc_no)
                print("account password : ",self.__acc_pass)
                
acc=Account("12678","neymar")
print(acc.acc_no)          
#print(acc.__acc_pass)  # its  give here erroe becuase acc_pass is private variable and i cannot access it directly out sided from the class we can access the password by using display method only
acc.display()