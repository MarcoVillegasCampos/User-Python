
from UserAccount import Account


class User:
    def __init__(self,fN="N/A",lN="N/A",age="N/A"):
        #Attributes
        self.firstName=fN
        self.lastName=lN
        self.age=age
        self.account=Account(accountNum=1234,balance=0)
        

    def printInfo(self):
        print(f"First name:{self.firstName}\nLast name:{self.lastName}\nAge: {self.age}")

    def deposit (self, amount):
        self.account+= amount
        return self

def withdraw (self, amount):
        if amount <= self.account:
            self.account -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.account}.")
            print(f"And you are trying to withdraw{amount}.")
        return self