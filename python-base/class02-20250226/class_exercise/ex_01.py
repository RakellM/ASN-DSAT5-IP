# Create a program that sells a bottle of water:
# - If the customer chooses natural mineral water, it will be charged R$1.50
# - If the customer chooses mineral water with gas, it will be charged R$2.50
# - If the customer chooses mineral water with lemon, it will be charged R$3.00

# %%
option_type = input("Choose the type of water you want to buy: \n"
                "1 - Natural mineral water\n"
                "2 - Mineral water with gas\n"
                "3 - Mineral water with lemon\n")

price = 0

option_qty = int(float(input("How many bottles of water do you want to buy?")))

if option_type == "1":
    price = 1.50
elif option_type == "2":
    price = 2.50
elif option_type == "3":
    price = 3.00

if price > 0 and option_qty > 0:
    total = price * option_qty
    print(f"Your total to pay is R${total:.2f}")
else:
    print("Invalid option.")
    



