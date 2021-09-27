from UserAccount import Account

class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "account1" : Account(.15,1000),
            "account2" : Account(.22,3000)
        }
        

    def display_balance(self):
        print(f"User: {self.name}, Account 1 Balance: {self.account['account1'].display_balance()}")
        print(f"User: {self.name}, Account 2 Balance: {self.account['account2'].display_balance()}")
        return self

   
   