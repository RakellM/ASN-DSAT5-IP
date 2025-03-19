# Write a program that receives an indefinite number of values corresponding to "account balance." However, when the user presses "Enter" without entering any value, the program stops receiving inputs and displays the sum of all previously entered values.

# %%

balance_sum = 0
balance_list = []

while True:
    balance = input("Enter account balance: ")
    if balance == "":
        break
    else:
        balance_list.append(float(balance))
        balance_sum += float(balance)

print(f"The account balances are {balance_list}.")
print(f"The sum of the account balances is {balance_sum:.02f}.")


# %%

balance_sum = 0
balance_list = []

while True:
    try:
        balance = float(input("Enter account balance: "))
    except ValueError:
        break
    balance_list.append(balance)
    balance_sum += balance

print(f"The account balances are {balance_list}.")
print(f"The sum of the account balances is {balance_sum:.02f}.")