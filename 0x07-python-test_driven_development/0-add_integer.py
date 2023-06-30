#!/usr/bin/python3
"""
a and b must be integers or floats
a and b must be first casted to integers if they are float
add_integer module
"""


def add_integer(a, b=98):
    """
    Addition Function
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return int(a + b)
