# 2.15 Write a program that receives a list of numbers from the user and counts how many times a specific number appears in the list. Ask the user for a number and display the count.

# %%

my_list = []

while True:
    user_input = input("Enter an integer number: ")

    if user_input == "":
        break

    try:
        nbr = int(float(user_input))     
        my_list.append(nbr)
    except ValueError:
        print("Please enter a valid number")

print("The list is: ", my_list)

user_nbr = input("Enter a number to count: ")

try:
    user_nbr = int(float(user_nbr))
except ValueError:
    print("Please enter a valid number")

count_nbr = my_list.count(user_nbr)

print(f"The number {user_nbr} appears {count_nbr} times in the list.")


