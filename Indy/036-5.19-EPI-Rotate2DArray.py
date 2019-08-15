"""
Input: An nXn 2D array/matrix
Output: Array rotated clockwise by 90 degrees
Logic:
    - Transpose the matrix
    - For clockwise rotation - reverse the rows
    - For anticlockwise rotation - reverse the columns
"""

from typing import List

class Solution:
    def rotate_matrix_by_90(self, input2D_Arr: List[List[int]]) -> None:

        # transpose function
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse function - reverses col
        def reverse_col(matrix):
            for i in range(len(matrix)):
                j, k = 0, len(matrix)-1
                while j < k:
                    matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i]
                    j, k = j+1, k-1

        # print matrix function
        def print_matrix(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    print(str(matrix[i][j]), end=" ")
                print()

        transpose(input2D_Arr)
        reverse_col(input2D_Arr)
        print_matrix(input2D_Arr)


s = Solution()
arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
s.rotate_matrix_by_90(arr)
