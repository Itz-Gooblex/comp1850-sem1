# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width:float, height:float):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if type(width) not in [float,int]:
            raise TypeError("Width is not a number")
        if width <= 0:
            raise ValueError("Width is not a natural number")

        if type(height) not in [float,int]:
            raise TypeError("Height is not a number")
        if height <= 0:
            raise ValueError("Height is not a natural number")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        '''Returns true if distance are equal -> rectangle is square'''
        return self.width == self.height

    def area(self):
        '''Returns product of width and height'''
        return self.width * self.height

    def perimeter(self):
        '''Returns sum of width and height doubled'''
        return 2*(self.width + self.height)
    # (See README.md for details of what they should do)
