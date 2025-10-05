# Brandon Claypool
# 10/05/25
# P2LAB1
# This program asks the user for the radius of a circle, 
# then calculates and displays the diameter, circumference, and area.

import math

# Pseudocode:
# 1. Ask user for the circle's radius (float)
# 2. Calculate diameter, circumference, and area using formulas
# 3. Display the results formatted to 1, 2, and 3 decimal places

# Ask user for the radius
radius = float(input("What is the radius of the circle? "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with proper formatting
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
