class bankaccount:
    def __init__(self,name,id,balance=0):
        self.name=name
        self.id=id
        self.balance=balance
    def deposit(self ,amount):
        self.amount=amount
        if amount > 0 :
            self.balance+=amount
            return f"deposited {amount} and your new balance is equall to {self.balance}"
        
    def withdraw(self,amount):
        self.amount=amount
        if amount > 0 and amount <= self.balance:
            self.balance-=amount
            return f"with draw amount : {self.amount} and new balance is equall to {self.balance}"
        else:
            print("insuffecent balance")
a1=bankaccount("jawad ali",12345,1000)
print(a1.deposit(1000))
print(a1.withdraw(500))
        
    
