# Create a code that checks if the item that a person selected to buy at the store is one of the following: orange, beer, instant noodles, coal, rump steak.

# %%

# TODO: correct plural and singular to also match the items in the list.
items_to_flag = ["orange", "beer", "instant noodles", "coal", "rump steak"]

list_items = []

print("List all the items you plan to buy at the store.")
print("When you finish, type 'enter'.\n")

while True:
    to_buy_items = input("Enter the item you want to buy: ")
    if not to_buy_items:
        break
    list_items.append(to_buy_items)

for item in list_items:
    if item.lower() in items_to_flag:
        print(f"{item} is in the list of items to flag.")  

print(list_items)


