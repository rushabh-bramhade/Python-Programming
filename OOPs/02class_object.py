class Car:
    def __init__(self, brand , model):
        self.brand = brand 
        self.model = model

my_car = Car("TATA","G20")
print(f" Brand : {my_car.brand}  Model : {my_car.model}")


my_new_car = Car("farari","V200")
print(my_new_car.model)