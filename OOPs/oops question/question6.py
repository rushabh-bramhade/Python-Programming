"""
🔹 Q6 (Advanced)
Create class Employee

Constructor: id, name, salary

Method raise_salary(percent)

Prevent salary from becoming negative
"""

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def raise_salary(self,percent):
        if self.salary <= -0 or self.salary <= -1:
            print(f"{self.salary} You can not put your salary in negative!")
            print("  ")
        
        Ammount = self.salary / percent * 100
        print(f"Your salary percent is : {Ammount}")

emp_1 = Employee("emp1","rushabh",553)
emp_1.raise_salary(20)



    

