# Create a script that counts how many times the letter "a" appears in the word.

# %%

word = input("Type a word: ")

count = 0

for letter in word.lower():
    if letter == "a":
        count += 1

print(f"The letter 'a' appears {count} times in the word '{word}'.")

# %%

word = input("Type a word: ")

count = word.lower().count("a")

print(f"The letter 'a' appears {count} times in the word '{word}'.")
