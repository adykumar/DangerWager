"""
Input: Cyclically sorted input array
Output: Find the index of the smallest element in the array. O(log N) complexity
Logic: The array is cyclically sorted i.e. there is an inversion point somewhere in the array.
We use binary search to find the inversion.
if a[m] > a[n-1] (inversion) then minimum value must be between m and n-1
and if a[m] < a[n-1] (no inversion) then minimum value cannot be between m and n-1
"""

from typing import List

class Solution:
    def search_rotated_sorted_array(self, A: List[int]) -> int:

        # initialize the start and ends
        left, right = 0, len(A)-1

        # look for inversions until start and ends cross or the array is exhausted
        while left < right:
            mid = (left+right)//2
            if A[mid] > A[right]:  # if reversal present, the smallest element is in the right subarray
                left = mid+1
            else:  # else the reversal is in LHS and the smallest element is in the 1st subarray
                right = mid

        # left and right have crossed
        return left

s = Solution()
input = [378,478,550,631,103,203,220,224,279,368]
ans = s.search_rotated_sorted_array(input)
print("Index: "+ str(ans) + ", element: "+ str(input[ans]))

input = [1,203,220,224,279,368]
ans = s.search_rotated_sorted_array(input)
print("Index: "+ str(ans) + ", element: "+ str(input[ans]))

input = [1,103,203,220,224,279,368,-378,-278,-50]
ans = s.search_rotated_sorted_array(input)
print("Index: "+ str(ans) + ", element: "+ str(input[ans]))
