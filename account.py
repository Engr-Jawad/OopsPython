class Account:
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.__balance=balance
    def show_balance(self):
        return self.__balance
    def show_account_deatails(self):
        return f"Account holder name : {self.holder_name}\nAccount balance : {self.show_balance()}"

a1=Account("jawad ali",50000)
print(a1.show_account_deatails())