"""
Input: A permutation
Output: The next permutation according to dictionary ordering. If it is the last permutation, return an empty array.
Logic:
    - Start from the end, follow the non-decreasing sub-array from R -> L and find the first decreasing element
    - Now starting from this element move L -> R and find the first element greater than this element. Swap them.
    - Now reverse this sub-array (swapped element+1 : end) to get the next permutation

Example:
    - 6,2,1,5,4,3,0 => First decreasing element : 1
    - First element greater than 1 : 3
    - Swap: 6,2,3,5,4,1,0
    - Reverse the subarray: 6,2,3,0,1,4,5
"""
from typing import List


class Solution:
    def next_permutation(self, input: List[int]) -> List[int]:
        # Start R->L and find the first element smaller than it's previous entry
        inversion = len(input)-2
        while(inversion >= 0 and input[inversion] >= input[inversion+1]):
            inversion -= 1

        # if we didn't find any inversion point, this is the max permutation. Return empty array
        if inversion == -1:
            return []

        # find the smallest element greater than the inversion from R->L (in the sub-array) and swap with inversion
        for i in reversed(range(inversion+1, len(input))):
            if input[i] > input[inversion]:
                input[inversion], input[i] = input[i], input[inversion]
                break

        # now reverse the array from the index after the inversion to get the next dictionary permutation and return
        input[inversion+1:] = reversed(input[inversion+1:])
        return input


s = Solution()
print(s.next_permutation([6,2,1,5,4,3,0]))
print(s.next_permutation([6,7,8]))
print(s.next_permutation([8,7,6]))
