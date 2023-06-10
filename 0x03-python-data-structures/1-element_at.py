#!/usr/bin/python3

def element_at(my_list, idx):
    '''retrieves an element from a list'''
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        a = my_list[idx:idx+1]
        return a[0]
