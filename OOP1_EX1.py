class Simple_Bank_Account:

    def __init__(self, account_holder:str, initial_balance):
        self.account_holder=account_holder
        self.initial_balance=initial_balance
        self.balance=self.initial_balance

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.initial_balance+amount

    def withdraw(self, amount):
        self.amount=amount
        if self.balance>amount:
            self.balance=self.balance-amount
        else:
            print("Your Account Balance are lower then withdraw amount.")

    def get_balance(self):
        return self.balance

sba=Simple_Bank_Account("Ripon",100)
print(sba.account_holder)
print(sba.get_balance())
sba.deposit(500)
print(sba.get_balance())
sba.withdraw(500)
print(sba.get_balance())

