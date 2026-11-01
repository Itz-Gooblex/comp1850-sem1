# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    # Add distance() method here
    def distance(self):
        return (self.x**2 + self.y**2)**0.5
    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p = Point(3, 4)
print(p.distance())
