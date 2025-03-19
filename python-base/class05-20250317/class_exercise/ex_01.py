
# Reference for exercise 2.13
# Write a program that receives a number and displays its factorial.

# %%

def factorial(x):
    y = 1
    range_x = range(1, x + 1, 1)
    for i in range_x[::-1]:
        y *= i
        # print(i)
    
    return y

# %%

factorial(5)


# %%

# Correction 1

def factorial1(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    
    return result

factorial1(5)

# %%

# Correction 2

def factorial2(x):
    result = 1
    for i in range(x, 1, -1):
        result *= i
    
    return result

factorial2(5)

# %%

# TATTOO: A function should have one and only one objective.
