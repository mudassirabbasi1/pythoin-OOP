from bank_account import*

Mudassir = BankAccount(1000, "Mudassir")
liyar = BankAccount(2000, "liyar")

Mudassir.getbalance()
liyar.getbalance()

liyar.deposit(500)

Mudassir.withdraw(10000)
Mudassir.withdraw(10)


Mudassir.transfer(100000, liyar)
Mudassir.transfer(100, liyar)

ali = InterestRewardsAcct(1000, "ali")
ali.getbalance()
ali.deposit(100)
ali.transfer(100,Mudassir)

Adil = SavingsAcct(1000, "adil")
Adil.getbalance()
Adil.deposit(100)
Adil.transfer(1000, liyar)