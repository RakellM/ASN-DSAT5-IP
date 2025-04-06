# 2.16 Write a program that asks the user for a number and displays its multiplication table from 1 to 10.

# %%

while True:
    try:
        nbr = float(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number")


print(f"Multiplication table for {nbr}:")

for i in range(1, 11):
    mul = nbr * i
    print(f"{nbr} x {i} = {mul}")

# %%
