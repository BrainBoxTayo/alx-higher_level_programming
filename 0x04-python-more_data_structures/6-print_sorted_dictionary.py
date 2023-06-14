#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_sorted = sorted(a_dictionary)
    for i in a_sorted:
        print("{}: {}".format(i, a_dictionary.get(i)))
