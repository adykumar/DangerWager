"""

1065. Index Pairs of a String
Easy
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]
Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation:
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].


Note:

All strings contains only lowercase English letters.
It's guaranteed that all strings in words are different.
1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

"""

"""
Time- O(t*w) ??
Space- O(wl) where w words of avg length l is inserted into trie
"""

class Solution(object):

    def insertTrie(self, trie, w):
        temp = trie
        for ch in w:
            if ch not in temp:
                temp[ch]= {}
            temp= temp[ch]
        temp["end"]= len(w)

    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """

        trie= {}
        for w in words:
            self.insertTrie(trie, w)
        res= []
        for i in range(len(text)):
            temp= trie
            ch= text[i]
            if ch in temp:
                j= i
                while True:
                    if "end" in temp[ch]:
                        res.append([j-temp[ch]["end"]+1, j])
                    j+=1
                    temp= temp[ch]
                    if j >= len(text):
                        break
                    ch= text[j]
                    if ch not in temp:
                        break
        return res


        
