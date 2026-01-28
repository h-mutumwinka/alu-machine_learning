#!/usr/bin/env python3
"""
    A function that calculates the determinant of a matrix
"""


def determinant(matrix):
    """
        fucntion to calculate determinant
    """
    # check if the matix is a list and if the items in the matix is also a list
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1  # Determinant of 0x0 matrix is 1 by convention

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(submatrix)

    return det
