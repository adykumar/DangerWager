"""
767. Reorganize String
Medium

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
"""
Time- O(n log n)- log n for each push into and pop from heap
Space- O(n)
"""

from heapq import heappush, heappop
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dic= {}
        for ch in S:
            if ch not in dic:
                dic[ch]= 1
            else:
                dic[ch]+=1
        h= []
        for each in dic:
            heappush(h, [-dic[each], each])
        a= heappop(h)
        if -a[0] > (len(S)+1)/2: return ""
        heappush(h, a)
        res= []
        while h:
            a= heappop(h)
            res.append(a[-1])
            a[0]+=1
            if h!=[]:
                b= heappop(h)
                res.append(b[-1])
                b[0]+=1
                if b[0]!=0: heappush(h, b)
            if a[0]!=0: heappush(h, a)
        return ''.join(res)
