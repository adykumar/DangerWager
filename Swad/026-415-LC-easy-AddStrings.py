"""
415. Add Strings
Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

"""
Time- O(n)  n is length of the longer string
Space =1
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1)<len(num2):
            num1, num2= num2, num1
        num1= list(num1)
        num2= list(num2)
        c= 0
        i= len(num1)
        j= len(num2)
        while i>0:
            j-=1; i-=1
            x= int(num1[i])
            y= 0 if j<0 else int(num2[j])
            temp= x+y+c
            c=0
            if temp>9:
                temp= temp%10
                c=1
            #print num1, num2, temp
            num1[i]= str(temp)
            #print num1, num2
        if c==1:
            return "1"+''.join(num1)
        return ''.join(num1)
