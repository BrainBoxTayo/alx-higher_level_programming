#!/usr/bin/python3
"""
inheritance learning module
"""


def inherits_from(obj, a_class):
    """is it the sub class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
