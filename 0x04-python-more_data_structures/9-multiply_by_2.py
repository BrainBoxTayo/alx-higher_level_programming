#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new = a_dictionary.copy()
    for i in a_new:
        a_new[i] = a_new[i] * 2
    return a_new
