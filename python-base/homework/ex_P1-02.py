# Write a program that receives a person's name and age. Then, display the message:
# "Hello [name], good to know you are [x] years old. Welcome!"

# %%
name = input("What is your name? ").title()
age = int(float(input("How old are you? ")))

print(f"Hello, {name}! Good to know you are {age} years old. Welcome!")
