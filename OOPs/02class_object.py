class Car:
    def __init__(self, brand , model):
        self.brand = brand 
        self.model = model

my_car = Car("TATA","G20")
print(f" Brand : {my_car.brand}  Model : {my_car.model}")


my_new_car = Car("farari","V200")
print(my_new_car.model)



class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
        
s1 = Student("rajay",19)
print(print(f"Student name : {s1.name} and rollno : {s1.rollno}"))