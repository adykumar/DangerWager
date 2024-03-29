"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

"""
Time- O(n*m)
SPace- 1
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        """STEP 1- TRANSPOSE"""
        rows= len(matrix)
        cols= len(matrix[0])
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]


        """STEP 2- FLIP OPERATION"""

        for row in matrix:
            i=0; j= cols-1
            while i<j:
                row[i], row[j]= row[j], row[i]
                i+=1; j-=1
