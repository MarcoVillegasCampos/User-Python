from User import User

Marco = User("Marco")
Juan = User("Juan")

Marco.account['account1'].deposit(1000)
Juan.account['account1'].deposit(1000)
Marco.display_balance()
Juan.display_balance()
Marco.account['account1'].transferences(1000,Juan.account['account1'])
