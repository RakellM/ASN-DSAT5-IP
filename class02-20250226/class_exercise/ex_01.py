# Create a program that sells a bottle of water:
# - If the customer chooses natural mineral water, it will be charged R$1.50
# - If the customer chooses mineral water with gas, it will be charged R$2.50

# %%
option = input("Choose the type of water you want to buy: \n1 - Natural mineral water\n2 - Mineral water with gas\n")

if option == "1":
    print("Your total to pay is R$1.50")
elif option == "2":
    print("Your total to pay is R$2.50")
else:
    print("Invalid option, please.\nChoose 1 (Natural mineral water) or 2 (Mineral water with gas)")