#!/usr/bin/python3

"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Function to rotate a matrix 90degs"""
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft

        right -= 1
        left += 1
