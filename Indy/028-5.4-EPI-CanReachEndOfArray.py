"""
Input: An array of n integers where A[i] denotes the max you can advance from index i
Output: Return whether it's possible to advance to the end
Logic:
- Maintain a running max of the index you can reach at every array index
- If you reach the last index at any point, short circuit and return true
"""

from typing import List


class Solution:
    def can_reach_end(self, A: List[int]) -> bool:
        # find the last index
        current_max_reach, last_index = 0, len(A)-1
        current_index = 0

        # process each index to find the max reach at that index and check if the last index is reachable
        while current_index <= current_max_reach and current_max_reach < last_index:
            current_max_reach = max(current_max_reach, A[current_index]+current_index)
            current_index += 1

        # if the max reachable index is greater than the last_index, return true else false
        return current_max_reach >= last_index

s = Solution()
print(s.can_reach_end([3,3,1,0,2,0,1]))
print(s.can_reach_end([3,-3,1,0,2,0,1]))
print(s.can_reach_end([3,2,0,0,2,0,1]))