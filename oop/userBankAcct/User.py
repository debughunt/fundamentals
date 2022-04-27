from bankAcct import BankAccount

class user:
    def __init__(self, acctName, checking_int = .01, saving_int = .01, checking_amt = 0, saving_amt = 0):
        self.name = acctName
        self.checking = BankAccount("checking", checking_int , checking_amt)
        self.savings = BankAccount("saving", saving_int, saving_amt)
    def make_deposit(self, acct, amount):
        if acct == "checking":
            self.checking.deposit(amount)
        elif acct == "savings":
            self.savings.deposit(amount)
        return self

    def make_withdrawal(self, acct, amount):
        if acct == "checking":
            self.checking.withdraw(amount)
        if acct == "checking":
            self.checking.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Account Balance: ${self.checking.account_bal}\n Savings Account Balance: ${self.savings.account_bal}")
        return self
    
    def transfer_money(self, other_user, amount):
        self.checking.account_bal -= amount
        other_user.checking.account_bal += amount
        return self


Guido = user('Guido van Rossum', checking_amt = 150)
Hunter = user('Hunter Ray', saving_amt= 500)
John = user('John Doe', checking_amt= 350, saving_amt= 200)

Guido.make_deposit("checking", 50).make_deposit("checking", 150).make_deposit("checking", 25).make_withdrawal("checking", 100).display_user_balance()

Hunter.make_deposit("savings", 50).make_deposit("savings", 100).make_withdrawal("savings", 25).make_withdrawal("savings", 30).display_user_balance()

John.make_deposit("checking", 200).make_withdrawal("savings", 25).make_withdrawal("checking", 25).make_withdrawal("checking", 25).display_user_balance() 

Guido.transfer_money(John, 100).display_user_balance()
John.display_user_balance()