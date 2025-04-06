# 2.12 Write a program that displays numbers from 1 to 100.
# - If the number is divisible by 3, display "**Fizz**". 
# - If the number is divisible by 5, display "**Buzz**". 
# - If the number is divisible by both, display "**FizzBuzz**".

# %%

nbrs = range(1, 101)

for i in nbrs:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


