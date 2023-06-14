#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    setx = set(my_list)
    for i in setx:
        j += i
    return j
