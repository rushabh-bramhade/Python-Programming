class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def display(self):
        print(f"Car Brand : {self.brand} Year : {self.year}")

class Electrical_car(Car):
    def __init__(self,brand,year,battery_size):
        super().__init__(brand,year)
        self.battery_size = battery_size

    def display(self):
        print(f"Car Brand : {self.brand} Year : {self.year} Battery Size : {self.battery_size}")

car_1 = Electrical_car("hsdk",34,34)
car_1.display()