"""
524. Longest Word in Dictionary through Deleting
Medium

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
"""
Time- O(ns) number of words in dict * length of main string
Space- O(1)
"""

class Solution(object):

    def compare(self, s, word, maxword):
        mw= maxword[0]
        if len(word)<len(mw): return
        #if len(s)<len(word): return
        if len(word)==len(mw) and mw<word: return

        j=0
        for ch in s:
            if ch==word[j]: j+=1
            if j==len(word):
                maxword[0]= word
                return

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxword= [""]
        for word in d:
            self.compare(s, word, maxword)
        return maxword[0]
        
