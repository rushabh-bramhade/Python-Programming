class BankAccount:
    def __init__(self,balance):
        self.__balance = balance  
    def get_balance(self):
        return int(self.__balance)
    def set_balance(self,balance):
        if balance >= 0:
            self.__balance = balance 
        else:
            print("Invaild amount")
bank1 = BankAccount(2334.3)
print(bank1.get_balance())
