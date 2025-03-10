# Redo exercise 2.4, but use a for loop and lists to receive the student’s grades.

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