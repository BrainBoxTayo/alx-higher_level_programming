#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0
    for i in sys.argv:
        j += 1
    if j == 2:
        print("{} argument:".format(j - 1))
    elif j == 1:
        print("{} arguments.".format(j - 1))
    else:
        print("{} arguments:".format(j - 1))
    for i in range(1, j):
        print("{}: {}".format(i, sys.argv[i]))
