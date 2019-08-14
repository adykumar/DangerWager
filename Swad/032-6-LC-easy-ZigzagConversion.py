"""
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

"""
Time- O(n)
SPace- O(n)
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s
        res= [[] for i in xrange(numRows)]
        i=0
        chunk= 2*numRows - 2
        while i<len(s):
            ch= s[i]
            pos= i%chunk
            if pos<numRows:
                res[pos].append(ch)
            else:
                res[-pos%numRows -2].append(ch)
            #print ch, pos, res
            i+=1
        Res= ""
        for r in res:
            Res+= ''.join(r)
        return Res
