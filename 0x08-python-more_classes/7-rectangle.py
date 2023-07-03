#!/usr/bin/python3
"""
Defines a Rectangle
"""


class Rectangle:
    """
    this is the class Rectangle
    attributes:
        __width: instance attribute
        __height: instance attribute
        number_of_instances: the number of instances of class Rectangle
    methods:
        area: returns area of the rectangle
        perimeter: returns the perimeter of the rectangle
    """
    number_of_instances = 0
    print_symbol = [1, 2, 3]

    # the Underscores
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        string = []
        for i in range(self.height):
            [string.append(str(self.print_symbol)) for j in range(self.width)]
            if i + 1 != self.height:
                string.append('\n')
        return ("".join(string))

    def __repr__(self):
        return ('Rectangle(' + str(self.width) + ', ' + str(self.height) + ')')

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    # decorated methods
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    # methods to calculate stuff
    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)
