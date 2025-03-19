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

fruit_list = {
    "apple": 1.50,
    "banana": 2.75,
    "grape": 1.90,
    "pear": 1.25,
    "orange": 0.65,
    "lemon": 1.25,
    "guava": 2.15,
    "pineapple": 3.20,
    "jackfruit": 5.80
}

fruit = input("Enter the name of a fruit: ").lower()

if fruit in fruit_list:
    print(f"R${fruit_list[fruit]:.2f}")
else:
    print("Fruit not found.")
