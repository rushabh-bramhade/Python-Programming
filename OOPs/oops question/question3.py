"""
🔹 Q3 (Intermediate)
Create class Student
Constructor takes name
Create method display() that prints name
Create 2 objects and call display()
"""

class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)

S1 = Student("Rushabh")
S1.display()
S2 = Student("sakasi")
S2.display()
