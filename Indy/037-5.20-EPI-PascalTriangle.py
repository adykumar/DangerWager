"""
Input: A number N
Output: Compute the Pascal triangle for this N

Logic:
    - Pascal triangle has N number of rows
    - The ith row has i elements
    - The element (0,0) starts with a 1
    - Next row is determined by: result[i][j] = result[i-1][j-1] + result[i-1][j]
"""

from typing import List


class Solution:
    def generate_pascal_triangle(self, n: int) -> List[List[int]]:

        # allocate the result grid
        # n rows where the i-th row has i elements
        # the first element in each row will always be 1
        result = [[1] * (i+1) for i in range(n)]

        for i in range(n):
            for j in range(1,i):
                # entry = sum of the adjacent entries in the row directly above
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

    def print_pascal_triangle(self, triangle: List[List[int]]):
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                print(triangle[i][j], end=" ")
            print()


s = Solution()
r = s.generate_pascal_triangle(5)
s.print_pascal_triangle(r)
