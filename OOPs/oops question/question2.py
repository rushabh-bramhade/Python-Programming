"""
🔹 Q2 (Beginner)
Create class Car
Constructor takes brand and year
Print both using object
"""

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def car_details(self):
        print(f"Car Brand : {self.brand} and Car year : {self.year}")

user_input_brand = input("Enter the car brand :")
user_input_year = int(input("Enter the car year :"))

car_1 = Car(user_input_brand,user_input_year)
car_1.car_details()