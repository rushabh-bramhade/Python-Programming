# Write a python program to display a user's enters name followed by Good Afternoon using the input() function

string_name = input("Enter your name :")

print("Good Afternoon : ", string_name)

# Write a pyton program to fill a letter template give below the name and date.
# letter = ''' Dear <| NAME |> You are seleted! <| DATE |> '''

letter = ''' Dear <| NAME |> You are seleted! <| DATE |> '''

letter = letter.replace(" NAME ", " Rushabh")
letter = letter.replace(" DATE ", " 03 aug 2026 ")

print(letter)

# Write a python program to detect double spaces in a string 

string_spaces = "hello  i   am rushabh"

print(string_spaces.find("   "))

# Replaces the double spaces from problem 3 with single spaces

string_spaces = string_spaces.replace("   ", " ")

print(string_name)

# Write a program to format the following letter using escape squences characters

letter_offer = "Dear Rushabh,\n\tThis Python course is nice.\nThanks!"

print(letter_offer)