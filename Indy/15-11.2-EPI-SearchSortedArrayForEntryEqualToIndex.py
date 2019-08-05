"""
Input: Sorted array of distinct integers
Output: Return an index i for which the element at i == index i
Example: Input: [-2,0,2,3,6,7,9], Output: 2 or 3
Logic:
We can prune the search space using the logic:
    - if A[j] > j, no element after j can be equal to A[j]
    - if A[j] < j, no element before j can be equal to A[j]
"""
from typing import List

class Solution:
    def search_entry_equal_to_index(self, input: List[int]) -> int:
        left, right = 0, len(input)-1

        # search until start and end cross over
        while left <= right:
            mid = (left+right)//2
            diff = input[mid] - mid

            # if diff == 0, return this index
            if diff == 0:
                return mid
            # if diff > 0 i.e. index is smaller than the value, prune right half of the array
            elif diff > 0:
                right = mid - 1
            else: # diff < 0 i.e. index is greater than the value at the index,  prune left side of the array
                left = mid+1


        # if not found, return -1
        return -1

s = Solution()
print(s.search_entry_equal_to_index([-2,0,2,3,6,7,9]))
print(s.search_entry_equal_to_index([-2,-1,0,1,6,7,9]))
print(s.search_entry_equal_to_index([-2]))
print(s.search_entry_equal_to_index([]))
print(s.search_entry_equal_to_index([1,1,1]))
print(s.search_entry_equal_to_index([0]))
