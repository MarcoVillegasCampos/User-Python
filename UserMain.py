from UserAccount import Account
from User import User

michaelUser=User("Michael", "Miller",30)
alvaroUser=User("Alvaro", "Sanchez",35)

michaelAccount= Account(12345, michaelUser)
michaelAccount=Account(5555,michaelUser)
alvaroAccount= Account(22222, alvaroUser)



michaelUser.deposit(1000)


#julieAccount= Account(54321, "Julie Sanders")

#michaelAccount.deposit(1000).deposit(1000).deposit(1000).withdraw(100).printBalance()


#alvaroAccount.deposit(1000).deposit(1000).withdraw(1000).withdraw(1000).printBalance()




#julieAccount.deposit(5000).withdraw(1000).withdraw(1000).withdraw(1000).printBalance()




#result= Account.transferMoney(michaelAccount,1000,julieAccount)
#michaelAccount.printBalance()
#julieAccount.printBalance()

