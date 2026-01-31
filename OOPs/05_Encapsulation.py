class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"hello your name is {self.name}"
obj = Animal("Rushabh")
print(obj) 