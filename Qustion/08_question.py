# Problem:
# Input N. Print the sum of numbers from 1 to N.

user_input = int(input("How many number do you want to store :"))
arr = [0] * user_input   # create list with 0 number because to store numbers if it's not than IndexError: list assignment index out of range

for i in range(user_input):
    number = int(input(f"Enter the number {i + 1} :"))
    arr[i] = number
print(arr)
total = 0
for num in arr:
    total += num

print("sum of total numbers :",total)





