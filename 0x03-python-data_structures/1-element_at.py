#!/usr/bin/python3

def element_at(my_list, idx):
    '''retrieves an element from a list'''
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    elif idx == len(my_list) - 1:
        a = my_list[idx:]
        return a[0]
    else:
        a = my_list[idx:idx+1]
        return a[0]
