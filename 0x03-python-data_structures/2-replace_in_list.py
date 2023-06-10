#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''Replaces elemnt of a list at a
    specified position'''
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
