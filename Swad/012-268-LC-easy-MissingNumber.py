"""
268. Missing Number
Easy

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""
Time- O(n)
Space- O(1)
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(len(nums)+1)
        for i in xrange(len(nums)-1):
            nums[abs(nums[i])]*= -1
        for i in xrange(len(nums)):
            if nums[i]>0:
                return i
        if nums[-1]>0:
            return len(nums)-1
        for i in xrange(len(nums)):
            if nums[i]==0:
                return i


        
