# Create a code that checks if a persons belongs to the "calvo" or "silva" family.

# %%
last_name = input("Enter your last name: ")

if last_name.lower() == "calvo":
    print("You belong to the Calvo family.")

elif last_name.lower() == "silva":
    print("You belong to the Silva family.")

else:
    print("You don't belong to the Calvo nor the Silva family.")