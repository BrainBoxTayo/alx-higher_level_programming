#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j == matrix[-1]:
                print("{:1d}".format(j), end="")
                continue
            print("{:1d} ".format(j), end="")
        print()
