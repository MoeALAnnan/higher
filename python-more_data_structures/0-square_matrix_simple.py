#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_squares = []
    for x in range(0, len(matrix)):
        squares = [y*y for y in matrix[x]]
        new_squares.append(squares)
    return (new_squares)
