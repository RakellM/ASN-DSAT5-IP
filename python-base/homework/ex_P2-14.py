# 2.14 Consider the following list:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]
# Write a program that returns the **position** of the smallest and largest values in the list:
# The highest value is at position x.
# The lowest value is at position y.

# %%

my_list = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

smallest_value = min(my_list)
largest_value = max(my_list)

smallest_position = my_list.index(smallest_value) + 1 
largest_position = my_list.index(largest_value) + 1 

# Print the results
print(f"The highest value is at position {largest_position}.")
print(f"The lowest value is at position {smallest_position}.")



