# Week 1.5, Session 2: Task 4
from geometry import *
# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

test_circle = Circle(5,Point(0,0))
test_point1 = Point(1,1)
test_point2 = Point(3,4)
test_point3 = Point(6,8)

print(test_point1 in test_circle)
print(test_point2 in test_circle)
print(test_point3 in test_circle)