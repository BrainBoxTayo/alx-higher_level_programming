#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    elif idx == len(my_list) - 1:
        del my_list[idx]
    else:
        del my_list[idx:idx+1]
    return my_list
