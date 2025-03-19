# #### 2.1 Write a program that receives a person's name and age.
# If the person is under 18 years old, display the message:
# ` "John, you cannot drive or drink." `
# For people between 18 and 65 years old, display:
# ` "John, drinking is allowed! Just don't drive!" `
# For people over 65 years old, display:
# ` "John, drink with great moderation!" `

# %%

name = input("What is your name? ").title()
age = int(float(input("How old are you? ")))

if not name:
    name = "Whoever you are"

if not age or age < 0:
    print("Please enter a valid age.")
    exit(1)

elif age < 18:
    print(f"{name}, you cannot drive or drink.")

elif age < 65:
    print(f"{name}, drinking is allowed! Just don't drive!")

else:
    print(f"{name}, drink with great moderation!")