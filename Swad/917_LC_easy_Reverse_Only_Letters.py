"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""

"""
Time: O(n)
Space: O(1)
"""

class Solution(object):

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        st= list(S)
        l= 0
        r= len(st)-1
        while l<r:
            if st[l].isalpha() and st[r].isalpha():
                st[l], st[r] = st[r], st[l]
                l+=1; r-=1
            if not st[l].isalpha():
                l+=1
                continue
            if not st[r].isalpha():
                r-=1
        return ''.join(st)
