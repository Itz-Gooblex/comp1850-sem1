# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import *

test_circle = Circle(Point(0,0), 2.5)
print(test_circle)
print(f"Area = {test_circle.area()}")
print(f"Perimeter = {test_circle.perimeter()}")
print("Moving circle...")
test_circle.set_position(Point(1.6, 3.2))
print(test_circle)
test_circle.set_colour("green")
print(test_circle)