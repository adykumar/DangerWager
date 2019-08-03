"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

"""
Time: n* 2^n
Space: n/2 * 2^n
"""

class Solution(object):

    def backtrack(self, nums, start, curr, res):
        if start>len(nums):
            return
        temp= curr[::]
        res.append(temp)

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(nums, i+1, temp, res)
            temp.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res= []
        self.backtrack(nums, 0, [], res)
        return res
