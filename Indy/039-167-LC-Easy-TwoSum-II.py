"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Logic:
    - We use two pointers (one from each end) to see if their sum == target
    - If:
        - it's equal to the target, return the indices (+1 since they are not zero based)
        - if it is < target, advance the left pointer
        - else, advance the right pointer
"""
from typing import List


class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


s = Solution()
print(s.twoSumII([2,7,11,15], 9))
print(s.twoSumII([2,77,121,150], 123))
print(s.twoSumII([-2,17,141,156], 139))
print(s.twoSumII([-2,17,141,156], 9))
