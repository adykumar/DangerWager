"""
93. Restore IP Addresses
Medium

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

"""
Time-  O(n* 2^n)
Space- O(n* 2^n)
"""

class Solution(object):

    def backtrack(self, s, start, dots, temp, res):
        if start>=len(s): return
        t= temp[::]
        if dots==3:
            chunk= s[start:]
            if len(chunk)>1 and chunk[0]=="0" or len(chunk)>3:
                return
            if int(chunk)>=0 and int(chunk)<256:
                t.append(chunk)
                res.append('.'.join(t))
                return
        for i in range(1, 4):
            chunk= s[start:start+i]
            if int(chunk)>=0 and int(chunk)<256:
                if len(chunk)>1 and chunk[0]=="0":
                    continue
                t.append(chunk)
                self.backtrack(s, start+i, dots+1, t, res)
                t.pop()



    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res= []
        self.backtrack(s, 0, 0, [], res)
        return res
        
