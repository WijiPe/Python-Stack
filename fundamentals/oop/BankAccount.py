class BankAccount:
    all_accounts = []
    def __init__(self, name, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
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


U1 = BankAccount('Jane', 0.01, 1000)
U2 = BankAccount('John', 0.05, 10000)




U1.deposit(10).deposit(20).deposit(30).withdraw(1070).yield_interest().display_account_info()

U2.deposit(50).deposit(100).withdraw(500).withdraw(30).withdraw(8).withdraw(20000).yield_interest().display_account_info()


print(BankAccount.all_accounts)
BankAccount.all_balances()