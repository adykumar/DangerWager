"""
7. Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res= 0
        n= abs(x)
        while n>0:
            b= n%10
            res= res*10 + b
            n/=10

        if x<0: res*= -1
        if res<-1*(2**31) or res>(2**31)-1: return 0
        return res
"""
"""
Time- O(n)- n is length of number
Space- 1
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res= 0
        n= abs(x)
        while n>0:
            b= n%10
            res= res*10 + b
            n/=10

        if x<0: res*= -1
        if res<-1*(2**31) or res>(2**31)-1: return 0
        return res
