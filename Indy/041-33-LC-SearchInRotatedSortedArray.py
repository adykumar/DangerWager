"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array. Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Logic:
    - Modified binary search to search and limit runtime to O(log N)
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # edge case
        if not nums:
            return -1

        left, right = 0, len(nums)-1

        while left <= right:  # <= for the case [4,5,6,7,8,0,1,2,3], 3)
            mid = (left+right)//2
            # print("left: "+str(left)+" right: "+str(right)+" mid: "+str(mid))  # debug

            # if mid is the required target
            if target == nums[mid]:
                return mid
            # if the left segment is the increasing segment
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:  # if the left segment is the rotated segment [13,14,1,2,3,5,6,8]
                if nums[mid] <= target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


s = Solution()
print(s.search([0,1,2,3,4,5,6], 5))
print(s.search([4,5,6,7,8,0,1,2,3], 5))
print(s.search([4,5,6,7,8,0,1,2,3], 3))
print(s.search([5,1,3], 3))
print(s.search([1,1,1,1,1], 3))
