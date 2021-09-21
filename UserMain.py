from UserAccount import Account

michaelAccount= Account(12345, "Michael Miller")
alvaroAccount= Account(22222, "Alvaro Sanchez")
julieAccount= Account(54321, "Julie Sanders")

michaelAccount.deposit(1000).deposit(1000).deposit(1000).withdraw(100).printBalance()


alvaroAccount.deposit(1000).deposit(1000).withdraw(1000).withdraw(1000).printBalance()




julieAccount.deposit(5000).withdraw(1000).withdraw(1000).withdraw(1000).printBalance()




result= Account.transferMoney(michaelAccount,1000,julieAccount)
michaelAccount.printBalance()
julieAccount.printBalance()

