#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(int(len(my_list) / 2)):
        a = my_list[i] 
        my_list[i] = my_list[len(my_list) - (i + 1)]
        my_list[len(my_list) - (i + 1)] = a
    for i in my_list:
        print("{:d}".format(i))

my_list=[2, 4, 1, 9, 6]
print_reversed_list_integer(my_list)
