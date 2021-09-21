from UserAccount import Account

michaelAccount= Account(12345, "Michael Miller")
alvaroAccount= Account(22222, "Alvaro Sanchez")
julieAccount= Account(54321, "Julie Sanders")
michaelAccount.deposit(1000)
michaelAccount.deposit(1000)
michaelAccount.deposit(1000)
michaelAccount.withdraw(100)
michaelAccount.printBalance()

alvaroAccount.deposit(1000)
alvaroAccount.deposit(1000)
alvaroAccount.withdraw(1000)
alvaroAccount.withdraw(1000)
alvaroAccount.printBalance()


julieAccount.deposit(5000)
julieAccount.withdraw(1000)
julieAccount.withdraw(1000)
julieAccount.withdraw(1000)
julieAccount.printBalance()



result= Account.transferMoney(michaelAccount,1000,julieAccount)
michaelAccount.printBalance()
julieAccount.printBalance()

