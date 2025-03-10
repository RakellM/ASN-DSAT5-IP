# Ask the user for the name of a fruit and display the corresponding price.
# - Apple: R$1.50
# - Banana: R$2.75
# - Grape: R$1.90
# - Pear: R$1.25
# - Orange: R$0.65
# - Lemon: R$1.25
# - Guava: R$2.15
# - Pineapple: R$3.20
# - Jackfruit: R$5.80

# %%
fruit = input("Enter the name of a fruit: ").lower()

if fruit == "apple":
    print("R$1.50")
elif fruit == "banana":
    print("R$2.75")
elif fruit == "grape":
    print("R$1.90")
elif fruit == "pear":
    print("R$1.25")
elif fruit == "orange":
    print("R$0.65")
elif fruit == "lemon":
    print("R$1.25")
elif fruit == "guava":
    print("R$2.15")
elif fruit == "pineapple":
    print("R$3.20")
elif fruit == "jackfruit":
    print("R$5.80")
else:
    print("Fruit not found.")
