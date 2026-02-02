# Q4. Create a program that prints the multiplication table of a given number.


def tables():
    while True:
        print("1 : Enter numbers.")
        print("2 : Exit.")
        
        choice = int(input(f"Enter your choices :"))
        if choice == 1:
            num = int(input("Enter your number :"))
            for i in range(1,11):
                print(f"{num} x {i} = {num * i}")
        if choice == 2:
            print("Program successfully exit.")
            break
        if choice == None or choice > 2:
            break 
tables()