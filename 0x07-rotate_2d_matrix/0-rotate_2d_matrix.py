#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Rotates 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       args:
          matrix
    """
    #transpose
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


    #reverse
    N=len(matrix)
    for i in range(N//2):
        for j in range(N):
            matrix[j][i],matrix[j][N-1-i]=matrix[j][N-1-i],matrix[j][i]       
