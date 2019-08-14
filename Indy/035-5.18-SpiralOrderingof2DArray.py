"""
Input: n X n 2D array
Output: The spiral ordering of this array
Logic:
    - The spiral ordering can be evaluated in a layer by layer basis.
    - For a n X n matrix, we add the
        - n-1 elements from row 1 (L -> R)
        - n-1 elements from col n (T -> B)
        - n-1 elements from row n in reverse (R -> L)
        - n-1 elements from col 1 in reverse (B -> T)
        - This shift can be modeled as a 4*2 array:
           [[0, 1]
            [1, 0]
            [0, -1],
            [-1, 0]]
    - We use a directional pointer to move the spiral cursor in the right direction. The direction pointer circles
    between [0:3] i.e. the 4 rows in the shift array
"""
from typing import List


class Solution:
    def matrix_in_spiral_order(self, matrix: List[List[int]]) -> List[int]:

        # create the shift array, direction pointers
        shift = [[0,1], [1,0], [0,-1], [-1,0]]
        direction = x = y = 0
        result = []

        # we go through each element in the matrix in a spiral order. Processed cells are marked with 0
        for _ in range(len(matrix)**2):
            result.append(matrix[x][y])
            matrix[x][y] = 0
            next_x, next_y = x+shift[direction][0], y+shift[direction][1]
            # print(next_x, next_y, len(matrix))

            # this is a valid cell and has not been processed yet, process it
            # Else change direction
            if(next_x not in range(len(matrix)) or
                next_y not in range(len(matrix)) or
                matrix[next_x][next_y] == 0
            ):
                direction = (direction+1) & 3  # to ensure circling from 0 -> 3
                next_x, next_y = x+shift[direction][0], y+shift[direction][1]

            x, y = next_x, next_y

        return result

s = Solution()
print(s.matrix_in_spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(s.matrix_in_spiral_order([[1]]))
print(s.matrix_in_spiral_order([[1,2,3],[5,7,8],[90,11,12]]))
