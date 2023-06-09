#!/usr/bin/python3
"""Class of type square with size attribute"""


class Square:

    """Representing a square"""

    def __init__(self, size=0):
        """initializer for class square"""
        self.__size = size

    @property
    def size(self):
        """Getter for __size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area for the square"""
        return (self.__size * self.__size)
