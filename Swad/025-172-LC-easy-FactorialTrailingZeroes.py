"""
172. Factorial Trailing Zeroes
Easy

Given an integer n, return the number of trailing zeroes in n!.
Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""

"""
Time- log n
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=5
        x=n
        res= 0
        while x/i>0:
            res+= x/i
            i*=5
        return res
