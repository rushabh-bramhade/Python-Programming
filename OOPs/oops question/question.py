""" 
Create a class Person
Constructor with no parameters
Set:
name = "Unknown"
age = 0
Create object and print values
"""


class Person:
    def __init__(self,name = "Unknown" , age = 0):
        self.name = name
        self.age = age

    def person_details(self):
        print(f"Person details \n \t Name : {self.name} Age : {self.age}")

user_name = input("Enter your name :")
user_age = int(input("Enter your age :"))

person1 = Person(user_name,user_age)
person1.person_details()

