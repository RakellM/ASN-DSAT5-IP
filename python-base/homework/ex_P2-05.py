# Consider the following list:
# [120, “Python”, 120.01, “asw”, False, [10,20]] 
# Write a program that returns the following information:
# - The element at position -1 in the list
# - The element in the first position of the list
# - The last character of the second element in the list

# Element -1: x 
# First element: y 
# Last character of the second element: z 

# %%
list = [120, "Python", 120.01, "asw", False, [10,20]]

print(f"Element -1: {list[-1]}")
print(f"First element: {list[0]}")
print(f"Last character of the second element: {list[1][-1]}")

