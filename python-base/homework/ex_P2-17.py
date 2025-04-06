# 2.17 Write a program that asks the user for a word and checks whether it is a palindrome (i.e., the same word when read backward).

# %%

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome."""
    # Remove spaces and convert to lowercase for comparison
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]

user_input = input("Enter a word: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

# %%

user_input = input("Enter a word: ")

if user_input == user_input[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
