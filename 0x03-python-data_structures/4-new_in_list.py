#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copycat = my_list.copy()
    if idx < 0:
        return copycat
    elif idx > len(my_list):
        return copycat
    else:
        copycat[idx] = element
        return copycat
