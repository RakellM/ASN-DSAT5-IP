# 2.10 Write a program that receives a number. This number corresponds to a position in the Fibonacci sequence: 1, 1, 2, 3, 5, ...
# Display the Fibonacci number that corresponds to the given position:
# “Position x corresponds to the number y.” 

# The Fibonacci sequence is defined as follows:
# F(1) = 1
# F(2) = 1
# F(n) = F(n-1) + F(n-2) for n > 2

# %%

while True:
    try:
        nbr = int(float(input("Enter a interger: ")))
        if nbr < 1:
            print("Please enter a positive integer")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

# using for loop
fib = 0
prev_fib = 0

for i in range(1, nbr + 1):
    if i == 1 or i == 2:
        fib = 1
    else:
        fib = fib + prev_fib
    prev_fib = fib

print(f"Position {nbr} corresponds to the number {fib}.")

# %%

while True:
    try:
        nbr = int(float(input("Enter a interger: ")))
        if nbr < 1:
            print("Please enter a positive integer")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

# using while loop

fib = 0
prev_fib = 0
i = 1

while i <= nbr:
    if i == 1 or i == 2:
        fib = 1
    else:
        fib = fib + prev_fib
    prev_fib = fib
    i += 1

print(f"Position {nbr} corresponds to the number {fib}.")

