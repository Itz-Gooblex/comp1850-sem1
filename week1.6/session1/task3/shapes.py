# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    def __init__(self, position, radius, colour="red"):
        # Inherit properties from Shapes class
        super().__init__(position, colour)
        # Define radius attribute
        self.set_radius(radius)

    def set_radius(self, new_radius):
        if type(new_radius) not in [float, int]:
            raise TypeError("Type cannot be converted into a radius")
        if new_radius <= 0:
            raise ValueError("Radius must be greater han zero")
        self.radius = new_radius

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        return f"{(math.pi*self.radius**2):.3f}"

    def perimeter(self):
        return f"{(math.tau*self.radius):.3f}"
