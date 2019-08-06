"""
Input: A non-negative integer (k)
Output: Returns the largest integer (x) whose square is <= the given integer
Logic:
If x^2 < k then any number < x cannot be the solution
If X^2 > k then any number > x cannot be the solution
Use binary search in the range [0..k] to prune the search space
"""

class Solution:
    def compute_square_root(self, k: int) -> int:

        # setup left and right ranges
        left, right = 0, k

        # binary search to prune the search space
        while left <= right:
            mid = (left+right)//2
            mid_sq = mid*mid

            # if mid squared is less than k, any element < k cannot be the ans
            if mid_sq <= k:
                left = mid+1
            # if mid squared is greater than k, any element > k cannot be the ans
            else:
                right = mid-1

        return left-1  # to account for mid+1 on L23 in case of equality


s = Solution()
print(s.compute_square_root(626))
print(s.compute_square_root(6))
print(s.compute_square_root(0))
print(s.compute_square_root(283417835629876))
