# 2.11 Write a program with a function that receives a sentence. For each word in the sentence, reverse the order of the letters. Display the result:
# This is the original sentence.
# sihT si eht lanigiro ecnetnes.

# %%

sentence = input("Enter a sentence: ")
# sentence = 'This is the original sentence'

new_sentence = ''

sentence_list = sentence.split()
new_sentence_list = []

for word in sentence_list:
    new_sentence_list.append(word[::-1])

new_sentence = ' '.join(new_sentence_list)

print(f"Original: {sentence}")
print(f"Modified: {new_sentence}")


