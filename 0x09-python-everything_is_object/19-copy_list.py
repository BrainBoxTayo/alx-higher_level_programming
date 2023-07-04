#!/usr/bin/python3
'''
returns a copy of a list
'''
def copy_list(l):
    if isinstance(l, list):
        new_l = l[:]
    return new_l
