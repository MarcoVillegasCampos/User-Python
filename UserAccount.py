class Account:
    bankName="Coding Dojo Bank"
    allBankAccounts=[]

    def __init__(self, accountNum, user ):
        self.accountNum=accountNum
        self.user=user
        self.balance= 0.0
        Account.allBankAccounts.append(self)
   
       

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.balance}.")
            print(f"And you are trying to withdraw{amount}.")
        return self

    def deposit (self, amount):
        self.balance+= amount
        return self
    
    def printBalance(self):
        self.user.printInfo()
        print(f"Account balance: {self.balance}.")
        print(f"Account balance: {self.balance}.")
        
        return self

    def transferMoney (self, amount, account):                  #(self, externalAccount, aountToTransfer)
        if amount >= self.balance:                              #if self.validateFunds ( amountToTransfer)
            print("We cannot process your transfer.")           # self.withdraw (amountToTransfer)
            print(f"The origin account has: {self.balance}.")   # externalAccount.deposit (amountToTransfer)
            print(f"And you are trying to transfer{amount}.")   #else:
        else:                                                   #print ("You don't have enough funds to transfer.")
                                                                #using created methods for more consistency
            self.balance -= amount
            account.balance += amount
        return self

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
