# 2.18 Write a program that asks the user for sentences. To stop, the user can simply press "Enter" without typing anything.
# Your program should display each sentence and how many times it was repeated.

# %% 
my_list = []

while True:
    user_input = input("Enter sentence: ")

    if user_input == "":
        break

    my_list.append(user_input)   

# my_list = ['oi', 'oi', 'ola', 'oi', 'bom dia', 'boa noite', 'bom dia', 'oi ola', 'boa tarde']

print(f"The list is: {my_list}\n")

sorted_list = sorted(my_list)

print("Sentence count:")
word_prev = " "

for word in sorted_list:
    if word == word_prev:
        continue   

    else:
        print(word, ":", my_list.count(word))

    word_prev = word





