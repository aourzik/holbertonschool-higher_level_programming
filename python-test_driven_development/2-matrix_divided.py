#!/usr/bin/python3
"""Module that divides all elements of a Matrix."""


def matrix_divided(matrix, div):
    """
    Divide the elements of a matrix.

    All elements must be integers or floats, otherwise
    it raises a TypeError exception.

    Return a matrix of the elements divided. 
    """
    if (not isinstance(matrix, list)
            or matrix == []
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    len_row = len(matrix[0])
    for row in matrix:
        if len(row) != len_row:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
