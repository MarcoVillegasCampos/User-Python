class Account:
    accounts = []
    def __init__(self,interestRate,balance):
        self.interestRate = interestRate
        self.balance = balance
        Account.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_balance(self):
        return f"{self.balance}"

    def interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interestRate)
        return self
    
    def transferences(self,externalAccount,amount):
        self.withdraw(amount)
        externalAccount.deposit(amount)
        self.display_balance()
        externalAccount.display_balance()
      
        return self.display_balance()
    

    @classmethod
    def displayAllAccounts(cls):
        for account in cls.accounts:
            account.display_balance()
            
            
            
