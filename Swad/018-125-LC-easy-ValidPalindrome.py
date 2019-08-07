"""
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

"""
Time- O(n)
Space - 1
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0; r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1; r-=1
        return True
