"""
278. First Bad Version
Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

"""
Time- O(log n)
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
