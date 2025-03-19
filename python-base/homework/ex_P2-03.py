# Write a program that asks the user for a name and age and creates a dictionary with this information. Then, display the dictionary.

# %%

name = input("Enter your name: ")

age = input("Enter your age: ")

if not age:
    print("Invalid age")
    exit(1)
else:
    age = int(float(age))
    if age < 0:
        print("Invalid age")
        exit(1)
    else:
        if not name:
            print("Invalid name")
            exit(1)
        else:
            person = {
                "name": name,
                "age": age
            }
            print(person)   