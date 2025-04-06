# 2.13 Write a program that receives a number and displays its factorial.

# %%

# no fuction

while True:
    try:
        nbr = int(float(input("Enter a number: ")))
        break
    except ValueError:
        print("Please enter a valid number")

fact = 1

for i in range(1, nbr + 1):
    fact *= i

print(f"The factorial of {nbr} is {fact}.")

