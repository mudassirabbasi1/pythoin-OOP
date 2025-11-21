class balanceException(Exception):
      pass

class BankAccount:
        def __init__(self, initialAmount, acctName):
            self.balance = initialAmount
            self.name = acctName
            print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
        def getbalance(self):
              print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")
        
        def deposit(self,amount):
              self.balance += amount
              print(f"\nDeposit Complete ")
              self.getbalance()

        def viableTransaction(self, amount):
              if self.balance >= amount:
                    return
              else:
                    raise balanceException(
                          f"\nSorry , account'{self.name}'only has a balance of ${self.balance:.2f}"

                    )
        def withdraw(self, amount):
            try:
                    self.viableTransaction(amount)
                    self.balance -= amount
                    print("\nwithdraw complete")
                    self.getbalance()
            except balanceException as error:
                print(f"\nwithdraw interrupted :'{error}'")


        def transfer(self, amount, account):
            try:
                  print('\n*******\n\nBeginning transfer...🚀 ')
                  self.viableTransaction(amount)
                  self.withdraw(amount)
                  account.deposit(amount)
                  print('\n transfer complete! \n\n*********')
            except balanceException as error:
                  print(f'\nTransfer interrrupted {error}')
    

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
          self.balance = self.balance + (amount * 1.05)
          print("\n deposit complete")
          self.getbalance()       


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
            super().__init__(initialAmount,acctName)
            self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee )
            self.balance = self.balance - (amount + self.fee)
            print("\n withdraw complete")
            self.getbalance()
        except balanceException as error:
              print(f'\n withdraw interupted:{error}')


        
            
                  