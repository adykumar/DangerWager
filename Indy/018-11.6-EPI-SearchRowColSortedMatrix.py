"""
Input: A 2D sorted array and a number. 2D sorted array - rows and columns are increasing
Output: Check if the number exists in the matrix
Logic:
Both rows and cols are sorted. For an m X n matrix,
    - if x > A[0][n-1], then x is greater than elements in Row 0. Row 0 is pruned from the search space
    - if x < A[0][n-1], then x is less than elements in Col n-1. Col n-1 is pruned from the search space
"""

from typing import List

class Solution:
    def search_in_sorted_matrix(self, A: List[List[int]], x: int) -> bool:
        # find the matrix dimensions. We start from row 0 and col n-1 and work our way forward
        row, col = 0, len(A[0]) - 1

        # search while valid row and cols exist
        while row < len(A) and col >= 0:
            # if the current element is equal to x
            if A[row][col] == x:
                return True
            # if x is greater than max of the current row, the current row can be eliminated
            elif A[row][col] < x:
                row += 1
            else:  # A[row][col] > x => if x is smaller than max of the current row, \
                    # the current col needs to be eliminated
                col -= 1

        # all rows/cols processed, the element not present and hence we return False
        return False

s = Solution()
matrix = [[-1,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]
print(s.search_in_sorted_matrix(matrix, 8))
print(s.search_in_sorted_matrix(matrix, 200))
print(s.search_in_sorted_matrix(matrix, 3))
print(s.search_in_sorted_matrix(matrix, 0))
