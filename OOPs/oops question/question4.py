"""
Q4 (Intermediate)
Create class Account
Constructor takes balance
If balance < 0 → set balance = 0
Method show_balance()
"""

class Account:
    
    def __init__(self,balance):
        self.balance = balance
    def user_balance(self):
        if user_balance_input <= 0.0:
            print(f"Your Account balances is : {self.balance} very poor eww")
        elif user_balance_input <= 100.0:
            print(f"Your Account balances is : {self.balance} middel calss preson")
        elif user_balance_input <= 1000.000:
            print(f"Your Account balances : {self.balance} rice person")


user_balance_input = float(input("Enter your account balances :"))
person1 = Account(user_balance_input)
person1.user_balance()
