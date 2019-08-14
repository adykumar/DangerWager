"""
Input: Given a partially filled Sudoku board, check if it's valid. 0 in a cell represents a blank/incomplete cell.
Validity: No duplicates in row/col/subgrid.
Output: True if it's valid, else false

Logic:
    - We check the 3 constraints individually for rows/columns and the sub-grid
    - Constraints: No duplicates
"""

from typing import List
import math

class Solution:
    def is_valid_sudoku(self, board: List[List[int]]) -> bool:

        # helper function
        def has_duplicate(block):
            # remove 0's as zero represents incomplete cells and will lead to false positives during duplicate check
            block = list(filter(lambda x: x != 0, block))
            # check if there are any duplicates and return T/F accordingly
            return len(block) != len(set(block))

        # get the board size
        n = len(board)

        # check for duplicates in rows and columns
        if any(
            has_duplicate([board[i][j] for j in range(n)]) or  # cols
            has_duplicate([board[j][i] for j in range(n)])  # rows
            for i in range(n)
        ):
            return False

        #
        # now check each sub-grid. If any of them has a duplicate return False (return all - check not has_duplicate())
        # example: for a 9X9 board => n=3
        # I, J values will range from [0:3] each
        # a, b values will range from :
        # I, J : 0,0 => a=[0:3], b=[0:3] => 1st sub-grid (0,0)
        # I, J : 0,1 => a=[0:3], b=[3:6] => 2nd sub-grid (0,1)
        # I, J : 0,2 => a=[0:3], b=[6:9] => 3rd sub-grid (0,2)
        # ....
        # and so on
        subgrid_size = int(math.sqrt(n))
        return all(
            not has_duplicate([
                board[a][b]
                for a in range(subgrid_size*I, subgrid_size*(I+1))
                for b in range(subgrid_size*J, subgrid_size*(J+1))
            ])
            for I in range(subgrid_size)
            for J in range(subgrid_size)
        )


s = Solution()
print(s.is_valid_sudoku([[1,0,3,0],[0,2,0,1],[4,0,0,3],[0,0,1,0]]))
print(s.is_valid_sudoku([[1,0,3,0],[0,2,0,1],[4,0,0,3],[4,0,1,0]]))