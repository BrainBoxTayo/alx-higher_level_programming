#!/usr/bin/python3
"""
inheritance learning module
"""


def is_same_class(obj, a_class):
    """is it the same class"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
