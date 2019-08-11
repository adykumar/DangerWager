"""
238. Product of Array Except Self
Medium
<<<<<<< HEAD

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
=======
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

>>>>>>> 64d087befa2a8d227a075911838327f1e7b3f318
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""
<<<<<<< HEAD
Time= O(n)
Space= O(n)
=======
Time- O(n)
Space- no extra except result Array
>>>>>>> 64d087befa2a8d227a075911838327f1e7b3f318
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right=nums[-1]
        res= [1]
        for each in nums[:len(nums)-1]:
            res.append(res[-1]*each)
        i= len(res)-2
        while i>=0:
            res[i]*= right
            right*= nums[i]
            i-=1
        return res
<<<<<<< HEAD

        
=======
>>>>>>> 64d087befa2a8d227a075911838327f1e7b3f318
