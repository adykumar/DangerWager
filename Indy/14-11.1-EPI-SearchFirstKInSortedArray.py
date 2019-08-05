"""
Input: A sorted array and a key K
Output: Index of the first occurrence of "K" in the input array
Logic:
Use binary search to prune the search space to a candidate set of indices.
"""

from typing import List

class Solution:
    def search_first_k_in_sorted_array(self, input: List[int], k: int) -> int:
        left, right, result = 0, len(input)-1, -1

        # start binary search and continue until left and right pointers cross
        while left <= right:
            mid = (left+right)//2

            if input[mid] > k: # if mid is greater than the given k, prune right half of the array
                right = mid-1
            elif input[mid] == k: # mid is same as k, mark this as the current result and search in left subarray
                result = mid
                right = mid-1
            else: # mid is less than k, prune left half of the array
                left = mid+1
        return result

s = Solution()
print(s.search_first_k_in_sorted_array([1,3,5,6,8,8,8,8,12,15,18], 8))
print(s.search_first_k_in_sorted_array([1,3,5,6,8,8,8,8,12,15,18], 9))
print(s.search_first_k_in_sorted_array([], 8))
