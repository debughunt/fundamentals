class BankAccount:
# don't forget to add some default values for these parameters!
    def __init__(self, acct, int_rate = .01, amount = 0): 
        self.name = acct
        self.interest = int_rate
        self.account_bal = amount
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.account_bal += amount
        return self
    def withdraw(self, amount):
        self.account_bal -= amount
        return self
    def display_account_info(self):
        print(f"Your balance: {self.account_bal} \n Your Interest Rate: {self.interest}")
        return self
    def yield_interest(self):
        if self.account_bal > 0:
            self.account_bal = self.account_bal * self.interest
        return self



# Hunter = BankAccount('Hunter', balance = 500)
# John = BankAccount('John', .02, 350)

# Hunter.deposit(25).deposit(100).deposit(50).withdraw(60).yield_interest().display_account_info()

# John.deposit(100).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()