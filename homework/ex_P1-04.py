# Write a program that receives two values, A and B. Calculate the sum of these two values and return the result:
# Sum:  x.xx

# %%

while True:
    try:
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        total = a + b
        print(f'Sum: {total:.2f}')
        break
    except ValueError:
        print('Please enter a valid number')