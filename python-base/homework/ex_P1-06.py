# Write a program that receives a number in seconds, converts this number to hours, minutes, and seconds. Examples:
# Input: 556
# Output: 0:9:16
# Input: 140153
# Output: 38:55:53

# %%

number = int(float(input("Enter a number in seconds: ")))

if not number:
    print("Enter a valid number.")
elif number < 0:
    print("Enter a positive number.")
else:
    hours = number // 3600
    minutes = (number % 3600) // 60
    seconds = number % 60
    print(f"{hours}:{minutes}:{seconds}")