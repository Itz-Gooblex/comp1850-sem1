# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
from geometry import Circle, Point

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
centre = Point(1,1)

#  - Creates a Circle object, using the Point object and a value for radius
circle = Circle(centre, 5)

#  - Displays the area of the circle
print(circle.area())
print(circle.perimeter())
#  - Displays the perimeter of the circle
