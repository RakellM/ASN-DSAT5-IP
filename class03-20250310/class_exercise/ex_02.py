# Write a program that receives 4 height values using a loop and calculates their sum.

# %%

height_list = []
height_sum = 0

# TODO: fix for ValueError

for i in range(4):
    height = float(input("Enter height: "))
    height_list.append(height)
    height_sum += height

print(f"The heights are {height_list}.")
print(f"The sum of the heights is {height_sum:.02f}.")


# %% 

height_sum = 0

count = 1

while count <= 4:
    height_sum += float(input("Enter height: "))
    count += 1

print(f"The sum of the heights is {height_sum:.02f}.")