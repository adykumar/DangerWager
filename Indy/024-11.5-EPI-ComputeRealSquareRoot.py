"""
Input: A floating point number (X)
Output: It's square root
Logic: Use binary search to prune the search space - if a number (Y) is too big to be sq root of X, prune the space >= Y
Similarly if a number (Y) is too small to be the sq root of x, prune the space < Y
Start with the range [1.0, X] when X > 1.0 and [X, 1.0] if X < 1.0
"""

import math

class Solution:
    def compute_real_square_root(self, x: float) -> float:
        left, right = (x, 1.0) if x < 1.0 else (1.0, x)

        # stopping condition is left == right - as close as possible
        while not math.isclose(left, right):
            mid = 0.5 * (left + right)
            mid_sq = mid * mid

            # if current mid's sq is > x, then the sq root must be less than mid. Prune right search space
            if mid_sq > x:
                right = mid
            else: # means sq root is greater than mid, prune the left search space
                left = mid

        return left


s = Solution()
print(s.compute_real_square_root(67.987))
