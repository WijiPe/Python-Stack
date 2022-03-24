class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):	
        self.amount += amount
        return self
    
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.amount}")
        return self

    def transfer_money(self, amount, User):
        self.amount -= amount
        User.amount += amount
        self.display_user_balance()
        User.display_user_balance()
        return self


U1 = User('Jane')
U2 = User('John')
U3 = User('James')

U1.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawal(5).display_user_balance()


U2.make_deposit(100).make_deposit(1000).make_withdrawal(50).make_withdrawal(500).display_user_balance()

U3.make_deposit(1000).make_withdrawal(50).make_withdrawal(500).display_user_balance()

U1.transfer_money(10, U3)