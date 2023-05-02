#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    else:
        for x in matrix:
            for y in range(len(x) - 1):
                print("{:d}".format(x[y]), end=" ")
            for k in range(0, len(x)):
                if k == len(x)-1:
                    print("{:d}".format(x[k]))
            print()
