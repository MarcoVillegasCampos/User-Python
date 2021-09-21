from User import User

adrien = User("Adrien")

adrien.account['checking'].deposit(100)
adrien.display_user_balance()