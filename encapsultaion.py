#  ENCAPSULTION mena both information structure and its implementation details of its operations are hidden from outer world or wrapping data and function into a single unit (object) or to make capsule 
class Acct:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        
    def debit(self,amount):
        self.balance-=amount
        print("this amount" ,amount ,"from your account is deposit ")
        print("the total balance in your account is = ",self.get_balance())
        
    def credit(self,amount):
        self.balance+=amount
        print(f"this amount {amount}  is credit  ")
        print("the total balance in your account is = ",self.get_balance())
    
    def get_balance(self):
        return self.balance
    
    
acc1=Acct(1000,45632)
acc1.debit(500)
acc1.credit(1000)

    