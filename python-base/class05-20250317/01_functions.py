# %%

# Normal function:

# f(x ; mu , sigma) = (1 / sigma * sqrt(2 * pi)) * exp( (-1 / 2) * ((x - mu) / sigma) **2 )

# Where:
# mu -> mean of the population
# sigma -> standard deviation of the population
# x -> variable

# %%

# Usind a simple function for testing
# f(x) = x ** 2

def f_square(x):
    return x ** 2

# %%

f_square(9)

# %%
#--Function with obligatory arguments
def normal(x, mu, sigma):
    return ((1 / (sigma * (2 * 3.1415) ** 0.5))) * 2.71 ** ( (-1 / 2) * ((x - mu) / sigma) ** 2 )

# %%
print(normal(-1 , 0 , 1))
print(normal(-1 , 10 , 1))

# %%
#--Function with optional arguments
#--obligatory arguments have to be in front of optional arguments
def normal(x, mu=0, sigma=1):
    return ((1 / (sigma * (2 * 3.1415) ** 0.5))) * (2.71 ** ( (-1 / 2) * ((x - mu) / sigma) ** 2 ))

# %%
print(normal(-1 , 0 , 1))
print(normal(-1 ))

# %%

# Function to sort numbers into even or odd

def is_even(x: int):
    """
    is_even: function to show if a given number is even or odd.

    x: is an integer

    There is no return on this function.
    """
    if x % 2 == 0:
        print(f"{x} is even!")
    else:
        print(f"{x} is odd!")

# %%

is_even(7)

# %%
is_even("dois")

#--There is no way to enforce a type for the arguments.
#--The function will accept any arguments and it will breat in the operational part.
#--Using `: int` to give hints to the user of what the function will be expecting to run correctly.


