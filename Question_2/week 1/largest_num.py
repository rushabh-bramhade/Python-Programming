# Q5. Write a program to find the largest of three numbers.



def largest_num():
    while True:
        print("1 : Enter the numbers.")
        print("2 : Exit.")
        choice = int(input("Enter the choice :"))
        if choice == 1:
            num1 = int(input("Enter first number :"))
            num2 = int(input("Enter Second number :"))
            num3 = int(input("Enter Thrid number :"))

            if num1 >= num2 and num1 >= num3:
                print(f"{num1} is largest number.")
            elif num2 >= num1 and num2 >= num3:
                print(f"{num2} is largest number.")
            elif num3 >= num1 and num3 >= num2:
                print(f"{num3} is largest number.")
            elif num1 == num2 == num3:
                print(f"All numbers are equal {num1} , {num2} , {num2}")
                
        elif choice == 2:
            print("Program successfully executed!...")
            break


largest_num()