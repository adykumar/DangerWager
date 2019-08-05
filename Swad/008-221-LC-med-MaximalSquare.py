"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

"""
Time- O(n)
Space- O(1)
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0: return 0
        Max=0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]=="1":
                    v= 1+min(int(matrix[i-1][j-1]), int(matrix[i][j-1]), int(matrix[i-1][j]))
                    matrix[i][j]= str(v)
                    Max= max(Max, v)
        if Max==0:
            for row in matrix:
                if "1" in row: return 1
        return Max**2
