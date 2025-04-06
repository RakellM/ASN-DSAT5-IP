# 2.9 Write a program that receives a number. Check whether this number is prime or not and return the result:
# "The number x is prime." ` or ` "The number x is not prime." `

# %%

while True:
    try:
        nbr = int(float(input("Enter a number: ")))
        break
    except ValueError:
        print("Please enter a valid number")

if nbr <= 1:
    print(f"The number {nbr} is not a prime number.")
else:
    for i in range(2, int(nbr ** 0.5) + 1):
        if nbr % i == 0:
            print(f"The number {nbr} is not a prime number.")
            break
    else:
        print(f"The number {nbr} is a prime number.")

