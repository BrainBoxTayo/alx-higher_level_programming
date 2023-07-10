#!/usr/bin/python3
"""
inheritance learning module
"""


def is_kind_of_class(obj, a_class):
    """is it the same class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
