# Write a program that receives 4 student grades. Return the average of these grades, the lowest, and the highest grade:
# Average: x
# Lowest: y 
# Highest: z 

# %%

while True:
    try:
        grades = [float(input("Enter the grade of the student: ")) for i in range(4)]
        break
    except ValueError:
        print("Please enter a valid number")

average = sum(grades) / len(grades)
lowest = min(grades)
highest = max(grades)

print("The list below are the grades of the students: ")
print(grades)
print()
print(f"Average: {average:.0f}")
print(f"Lowest: {lowest:.0f}")
print(f"Highest: {highest:.0f}")

