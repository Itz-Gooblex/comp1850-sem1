# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

# Add a definition for a Circle class here, giving it
class Circle:
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
    def __init__(self, centre:Point, radius:float):
        self.centre = centre
        self.radius = radius
    
#  - A method area(), returning the area of the circle
    def area(self):
        return math.pi * self.radius**2

#  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self):
        return math.tau * self.radius 

# Don't add any testing code to this file!
