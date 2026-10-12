# Project Title: 2D Distance Calculator
# Description: Calculates the distance between two points.
# How to run: python distance_calculator.py
# Input needed: x1, y1, x2, y2 coordinates.
# Sample output: The distance between (0.0, 0.0) and (3.0, 4.0) is: 5.00
# Author: Josiah Wesley Egusquiza

# Input coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using standard exponent operators instead of the math module
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# IMPROVED UPDATE: Output the formatted result with coordinate details
print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
