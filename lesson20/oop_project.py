from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.get_balance()
Sarah.get_balance()

Sarah.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(100, Sarah)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(1000, Sarah)
