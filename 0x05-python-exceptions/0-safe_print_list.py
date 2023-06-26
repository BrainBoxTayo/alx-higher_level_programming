#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            x = x - 1
        if i == x - 1:
            print('\n', end="")
    return x
