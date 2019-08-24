"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Logic:
    - We maintain a map between the complement for an element and the array index.
    - For every number in the array, check if it exists in the map. If yes, short circuit and return.
    - Else store it's index and it's complement (target - number) in the map.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]

        return [-1, -1]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,7,-11,15], 4))
print(s.twoSum([2,-7,11,15], -5))
print(s.twoSum([2,-7,11,15], 5))
