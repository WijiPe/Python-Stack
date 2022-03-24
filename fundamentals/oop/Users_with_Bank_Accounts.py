class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.there_are_sufficient_funds(self.balance,amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")  
        return self

    def display_account_info(self):
        print(f"BankAccount:{self.name}, Balance:{self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            return self

    @staticmethod
    def there_are_sufficient_funds(balance,amount):
        if (balance - amount) > 0:
            return True
        else:
            return False
    
    @classmethod
    def all_balances(self):
        for i in range(len(BankAccount.all_accounts)):
            print(f"Balance: {BankAccount.all_accounts[i].balance}")


class User:
    def __init__(self, name):
        self.name = name
        self.account_saving = BankAccount(int_rate=0.02, balance=0)
        self.account_checking = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, account_name, amount):
        if (account_name == 'saving'):	
            self.account_saving.deposit(amount)
        elif(account_name == 'checking'):
            self.account_checking.deposit(amount)	
    
    def make_withdrawal(self,account_name,amount):
        if (account_name == 'saving'):	
            self.account_saving.withdraw(amount)
        elif(account_name == 'checking'):
            self.account_checking.withdraw(amount)	
    
    def display_account(self):
        print(f"User:{self.name}, Saving Balance:{self.account_saving.balance}")
        print(f"User:{self.name}, Checking Balance:{self.account_checking.balance}")

    def transfer_money(self,account_name, amount, User):
        if (account_name == 'saving'):
            self.account_saving.balance -= amount
            User.account_saving.balance += amount
        elif(account_name == 'checking'):
            self.account_checking.balance -= amount
            User.account_checking.balance += amount
        self.display_account()
        User.display_account()


U1 = User('John')
U2 = User('Jane')
U3 = User('James')


U3.make_deposit('saving',10)
U3.make_deposit('checking',10)
U3.display_account()