# Write a program that receives two values, A and B. Calculate the power of these two values and return the result:
# a ^ b = z

# %%
while True:
    try:
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        total = a ** b
        print(f'a ^ b: {total:.2f}')
        break
    except ValueError:
        print('Please enter a valid number')