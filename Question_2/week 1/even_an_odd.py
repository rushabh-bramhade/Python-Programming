

def even_odd():
    while True:
        print("1 : Enter the numbers.")
        print("2 : Exit")
        choice = int(input("Enter your choice :"))
        if choice == 1:
            num = int(input("Enter the number:"))
            if num % 2 == 0:
                print(f"number {num} is a even number.")
            else:
                print(f"number {num} is a odd number.")
        if choice == 2:
            print("program is successfully finished.")
            break
even_odd()
