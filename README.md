# Project Title: 2D Distance Calculator
# Description: Calculates the distance between two points.
# How to run: python distance_calculator.py
# Input needed: x1, y1, x2, y2 coordinates.
# Sample output: The distance between the two points is: 5.00
# Author: [Your Name]

# Input coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using standard exponent operators instead of the math module
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Output the formatted result
print(f"\nThe distance between the two points is: {distance:.2f}")
