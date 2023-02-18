#!/usr/bin/python3

"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""

def rotate_2d_matrix(matrix):
    """Function to rotate a matrix 90degs"""

    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []
    for row in transposed:
        rotated.append(row[::-1])
     
rows = int(input('Enter number of rows: '))
cols  = int(input('Enter number of column: '))

matrix = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(cols)] for i in range(rows) ] 

print()
print('Given matrix :')

for row in matrix:
    print(row)

rotate_90 = rotate_2d_matrix(matrix)

print()
print('Matrix after rotated by 90 degree')

for row in rotate_90:
    print(row)