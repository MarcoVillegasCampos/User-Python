from UserAccount import Account
from User import User

michaelUser=User("Michael", "Miller",30)
alvaroUser=User("Alvaro", "Sanchez",35)

michaelAccount= Account(12345, michaelUser,30)
alvaroAccount= Account(22222, alvaroUser,35)

michaelAccount.transferMoney(1000,alvaroAccount)
#julieAccount= Account(54321, "Julie Sanders")

#michaelAccount.deposit(1000).deposit(1000).deposit(1000).withdraw(100).printBalance()


#alvaroAccount.deposit(1000).deposit(1000).withdraw(1000).withdraw(1000).printBalance()




#julieAccount.deposit(5000).withdraw(1000).withdraw(1000).withdraw(1000).printBalance()




#result= Account.transferMoney(michaelAccount,1000,julieAccount)
#michaelAccount.printBalance()
#julieAccount.printBalance()

