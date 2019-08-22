"""
720. Longest Word in Dictionary
Easy

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""

"""
Time- O(w) w: number of words
Space- O(wl) w: words, l: avg length of each  [for inserting in set]
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        Set= set()
        for w in words:
            Set.add(w)
        Max= ""
        flag= False
        for w in words:
            if len(w)<len(Max) or len(w)==len(Max) and w>Max:
                continue
            for i in range(1, len(w)):
                if w[:i] not in Set:
                    flag= True
                    break
            if flag:
                flag= False
                continue
            Max= w
        return Max
