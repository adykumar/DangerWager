"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Time- O(n)
Space- O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="": return 0
        dic= {}
        Max= 0
        r= 0
        l= -1
        while True:
            if r==len(s)-1 and r-l<Max:
                break
            ch= s[r]
            if ch not in dic:
                dic[ch]= 1
                Max= max(Max, len(dic))
                if r<len(s)-1: r+=1
            else:
                while ch in dic:
                    l+=1
                    ch2= s[l]
                    if ch2 in dic:
                        dic[ch2]-=1
                        if dic[ch2]==0: del dic[ch2]
                Max= max(Max, len(dic))
        return Max
