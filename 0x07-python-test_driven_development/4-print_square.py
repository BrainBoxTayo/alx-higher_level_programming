#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        raise ValueError('size must be >= 0')
    the_square = "#"
    for j in range(0, size):
        [print(the_square, end='') for i in range(0, size)]
        print()
