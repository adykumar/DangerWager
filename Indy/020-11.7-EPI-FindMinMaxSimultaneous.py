"""
Input: Array of n elements
Output: Find min and max elements in better than O(N) time
Logic:
Compare two elements at a time and create 2 disjoint sets of min and max candidates (n/2 candidates - n/2 comparisons)
Find the global min and max by doing a running comparision of the sets (n/2 - 1) comparisons for each
Min and max in 3*n/2 - 1  comparisons
"""
from typing import List
import collections

class Solution:
    MinMax = collections.namedtuple('MinMax', ('smallest', 'greatest'))

    def find_min_max(self, A: List[int]) -> MinMax:

        # helper comparison function
        def create_min_max(a, b):
            return self.MinMax(a, b) if a<b else self.MinMax(b, a)

        # base case: If # elements is <= 1, return same element
        if len(A) <= 1:
            return self.MinMax(A[0], A[0])

        # process 1 pair at a time to create the min and max sets and find the global min and max
        global_min_max = create_min_max(A[0], A[1])
        for i in range(2, len(A)-1, 2):
            local_min_max = create_min_max(A[i], A[i+1])
            global_min_max = self.MinMax(
                min(global_min_max.smallest, local_min_max.smallest),
                max(global_min_max.greatest, local_min_max.greatest)
            )

        # edge case: For odd # element array, we need to do a final comparison for the last element
        if len(A) % 2:
            global_min_max = self.MinMax(
                min(global_min_max.smallest, A[-1]),
                max(global_min_max.greatest, A[-1])
            )

        return global_min_max


s = Solution()
print(s.find_min_max([3,2,5,1,2,4]))
print(s.find_min_max([3,2,-5,-1,2,4]))
print(s.find_min_max([3]))
print(s.find_min_max([3,3]))
