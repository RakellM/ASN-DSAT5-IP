# 2.2 Write a program that receives a number. Check if the given number is even or odd. Display the result as follows:
# ` "The number x is odd." `
# ` "The number x is even." `

# %%

number = int(float(input("Enter a number: ")))

# TODO: fix decimals or message that converts to integer?

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
# %%
