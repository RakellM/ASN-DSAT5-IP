# Write a program that receives the radius of a circle in centimeters. Return to the user the area and perimeter of this circle in the following format:
# Area:  x.xx 
# Perimeter:  y.yy

# %%

import math

pi_ = math.pi

radius = float(input("Enter the radius of the circle in centimeters: "))

if radius <= 0:
    print("Please enter a positive number.")
    exit(1)
else:
    perimeter = 2 * pi_ * radius
    area = pi_ * radius ** 2

    print(f"Radius: {radius:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")



