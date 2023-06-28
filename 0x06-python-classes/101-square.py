#!/usr/bin/python3
"""Class of type square with size attribute"""


class Square:

    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializer for class square"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """print the square"""
        the_space = " "
        square_char = '#'
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(the_space, end="")
                for j in range(0, self.__size):
                    print(square_char, end="")
                print("")

    @property
    def position(self):
        """Position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter funciton"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(num >= 0 for num in value) or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __repr__(self):
        printable = []
        sub_print = ""
        if self.size == 0:
            return ""
        else:
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    sub_print += " " 
                for j in range(0, self.__size):
                    sub_print += "#"
                printable.append(sub_print)
                sub_print = ""
        return "\n".join(printable)
