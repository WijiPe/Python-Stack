class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):	
        self.amount += amount
    
    def make_withdrawal(self, amount):
        self.amount -= amount
    
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.amount}")

    def transfer_money(self, amount, User):
        self.amount -= amount
        User.amount += amount
        self.display_user_balance()
        User.display_user_balance()


U1 = User('Jane')
U2 = User('John')
U3 = User('James')

U1.make_deposit(10)
U1.make_deposit(20)
U1.make_deposit(30)
U1.make_withdrawal(5)
U1.display_user_balance()


U2.make_deposit(100)
U2.make_deposit(1000)
U2.make_withdrawal(50)
U2.make_withdrawal(500)
U2.display_user_balance()

U3.make_deposit(1000)
U3.make_withdrawal(50)
U3.make_withdrawal(500)
U3.display_user_balance()

U1.transfer_money(10, U3)