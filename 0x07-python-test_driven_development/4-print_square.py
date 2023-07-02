#!/usr/bin/python3
'''
print a square
'''


def print_square(size):
    '''
    Args:
        size: integer
    Returns:
        Nothing
    '''
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
