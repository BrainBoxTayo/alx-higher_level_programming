#!/usr/bin/python3
"""The square subclass of the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class for a square"""

    def __init__(self, size):
        """Initializer for the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
