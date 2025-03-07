# 3. Create a code of a Ice-Cream Store, where the user can choose:
#     a. Type of ice-cream: cone (`R$1.00`), large cone (`R$2,50`), basket (`R$4,00`)
#     b. Flavor of ice-cream: strawberry, vanilla, chocolate
#     c. Syrup: caramel (`R$1,50`), strawberry (`R$1,50`), chocolate (`R$1,50`), no syrup (`R$0,00`)
#     Present the total to be paid.

# %%
option_icecream = int(float(input("Choose the type of ice-cream you want to buy: \n"
                "1 - Cone\n"
                "2 - Large cone\n"
                "3 - Basket\n")))

option_flavor = int(float(input("Choose the flavor of ice-cream you want: \n"
                "1 - Strawberry\n"
                "2 - Vanilla\n"
                "3 - Chocolate\n")))

option_syrup = int(float(input("Choose the syrup you want: \n"
                "1 - Caramel\n"
                "2 - Strawberry\n"
                "3 - Chocolate\n"
                "4 - No syrup\n")))

if option_icecream < 1 or option_icecream > 3:
    print("Invalid option. Please, choose a valid ice-cream type.")
elif option_flavor < 1 or option_flavor > 3:
    print("Invalid option. Please, choose a valid ice-cream flavor.")
elif option_syrup < 1 or option_syrup > 4:
    print("Invalid option. Please, choose a valid syrup.")
else:
    if option_icecream == 1:
        total = 1.00
    elif option_icecream == 2:
        total = 2.50
    else:
        total = 4.00

    if option_syrup == 4:
        total += 0.00
    else:
        total += 1.50

    print(f"Your total to pay is R${total:.2f}")

