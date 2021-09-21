class Account:
    bankName="Coding Dojo Bank"
    allBankAccounts=[]

    def __init__(self, accountNum, owner ):
        self.accountNum=accountNum
        self.owner=owner
        self.balance= 0.0
       

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.balance}.")
            print(f"And you are trying to withdraw{amount}.")

    def deposit (self, amount):
        self.balance+= amount
    
    def printBalance(self):
        print(f"Account balance: {self.balance}.")

    def transferMoney (self, amount, account):
        if amount >= self.balance:
            print("We cannot process your transfer.")
            print(f"The origin account has: {self.balance}.")
            print(f"And you are trying to transfer{amount}.")
        else:
            self.balance -= amount
            account.balance += amount

    @classmethod
    def changeBankName(cls, newName):
        cls.bankName=newName
    
    @classmethod
    def printAllAccountInfo (cls):
        for account in cls.allBankAccounts:
            account.printInfo()

    @staticmethod
    def doesAccountHasMoreThan100 (account):
        if  account.balance >= 1000:
            return True
        else:
            return False
