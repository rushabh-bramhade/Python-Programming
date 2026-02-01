import datetime
user_name = input("Enter your name :")
user_age = input("Enter your age :")

class User_data:
    def __init__(self, user_name , user_age):
        self.user_name = user_name
        self.user_age = user_age
    def display(self):
        print(f"Hello {self.user_name} and your age is {self.user_age}")
        print(f"Todays is date {datetime.date.today()}")
obj = User_data(user_name , user_age)
obj.display()