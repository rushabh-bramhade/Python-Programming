from array import array 


user_input = int(input(f"Enter how many numbers you want to store in array :"))
arr = array('i',[0] * user_input)

for i  in range(user_input):
    num = int(input(f"Enter the number {i + 1} :"))
    arr[i] = num
       
    
print(arr)
