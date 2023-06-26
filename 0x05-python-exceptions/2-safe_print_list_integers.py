#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            x = x - 1
        except (IndexError):
            x = x - 1
            raise
    print("\n", end="")
    return x
