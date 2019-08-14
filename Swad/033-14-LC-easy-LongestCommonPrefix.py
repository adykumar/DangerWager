"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
Time- O(nl) number of words * average length
SPace- O(1)
"""

class Solution(object):

    def prefixer(self, a, b):
        if a=="" or b==[]: return []
        i=0; j=0
        #print a, b
        while a[i]==b[j]:
            i+=1; j+=1
            if i>=len(a) or j>=len(b): break
        return b[:i]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0: return ""
        if len(strs)==1: return strs[0]
        common= self.prefixer((strs[0]), list(strs[1]))
        for w in strs[2:]:
            common= self.prefixer((w), common)
            if common==[]:
                break
        return ''.join(common)
