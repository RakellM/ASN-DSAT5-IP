# Create a program that sells a bottle of water:
# - If the customer chooses natural mineral water, it will be charged R$1.50
# - If the customer chooses mineral water with gas, it will be charged R$2.50

# %%
option_type = input("Choose the type of water you want to buy: \n"
                "1 - Natural mineral water\n"
                "2 - Mineral water with gas\n")

option_qty = int(float(input("How many bottles of water do you want to buy?")))

price = 0

if option_type == "1":
    price = 1.50
elif option_type == "2":
    price = 2.50
else:
    print("Invalid option, please.\n"
        "Choose 1 (Natural mineral water) or 2 (Mineral water with gas)")

if option_qty < 1:
    print("Invalid quantity. Please, choose a positive number.")
else: 
    total = price * option_qty
    print(f"Your total to pay is R${total:.2f}")



