# CHALLENGE
# 1. Babylon Lottery
# Build a program that randomly draws a number between 1 and 15.
# The user has 3 chances to guess the number.
# After each attempt, inform whether the guess is higher or lower than the drawn number.
# If the user guesses correctly, congratulate them!

# %%

#--To satrt, let's fix the correct number and don;t mind with the number of tries.

chosen_nbr = 7

guess_nbr = int(float(input("Choose a number between 1 and 15: ")))

if guess_nbr == chosen_nbr:
    print("Congratulations! You have chosen the corret number!")

elif guess_nbr > chosen_nbr:
    print("Your guess is greater then the correct number, try a smaller one!")

else:
    print("Your guess is smaller then the correct number, try a greater one!")

# %%

#--Now let's implement the number of tries

chosen_nbr = 7

try_times = 3
for t in range(1, try_times + 1):
    guess_nbr = int(float(input("Choose a number between 1 and 15: ")))

    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")

# %%

#--Fixing the breaks and continues

chosen_nbr = 7

try_times = 3
for t in range(1, try_times + 1):
    guess_nbr = int(float(input("Choose a number between 1 and 15: ")))

    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")
        break

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")


# %%

#--Enforce the number to be between 1 and 15, keep asking until it gets at most 3 numbers in the desired range

chosen_nbr = 7

try_times = 3
for t in range(1, try_times + 1):
    guess_nbr = 0

    while not 1 <= guess_nbr <= 15:
        guess_nbr = int(float(input("Choose a number between 1 and 15: ")))
        continue

    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")
        break

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")
# %%

#--Check the input for strings

chosen_nbr = 7

try_times = 3
for t in range(1, try_times + 1):
    guess_nbr = 0

    while not 1 <= guess_nbr <= 15:
        try:
            guess_nbr = int(float(input("Choose a number between 1 and 15: ")))
        except ValueError:
            print("Input a valid number!!!")

    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")
        break

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")

# %%

#--Make the chosen number a random

import random

chosen_nbr = random.randint(1, 15)

try_times = 3
for t in range(1, try_times + 1):
    guess_nbr = 0

    while not 1 <= guess_nbr <= 15:
        try:
            guess_nbr = int(float(input("Choose a number between 1 and 15: ")))
        except ValueError:
            print("Input a valid number!!!")

    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")
        break

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")

# print(chosen_nbr)

# %%

#--Now, with the code working, let's beautify it

import random

def get_nbr():
    guess_nbr = 0
    while not 1 <= guess_nbr <= 15:
        try:
            guess_nbr = int(float(input("Choose a number between 1 and 15: ")))
        except ValueError:
            print("Input a valid number!!!")
    return guess_nbr

def check_nbr(guess_nbr, chosen_nbr):
    if guess_nbr == chosen_nbr:
        print("Congratulations! You have chosen the corret number!")
        return True

    elif guess_nbr > chosen_nbr:
        print("Your guess is greater then the correct number, try a smaller one!")

    else:
        print("Your guess is smaller then the correct number, try a greater one!")
    
    return False

def main():
    chosen_nbr = random.randint(1, 15)
    try_times = 3
    
    for t in range(1, try_times + 1):
        guess_nbr = get_nbr()
        if check_nbr(guess_nbr, chosen_nbr):
            break

if __name__ == "__main__":
    main()

# print(chosen_nbr)

# %%
