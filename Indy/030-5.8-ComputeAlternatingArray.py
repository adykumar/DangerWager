"""
Input: An array of N numbers
Output: Re-arrange the array to get a new array with alternating increasing/decreasing numbers
A0 <= A1 >= A2 <= A3 >= A4 .. and so on

16,12,30,13,15,26,70,18 =>
16, 12 => i=0, sort => 12, 16 (,30,13,15,26,70,18)
16, 30 => i=1, rev sort => 12,30,16 (,13,15,26,70,18)
16, 13 => i=2, sort => 12,30,13,16 (,15,26,70,18)
16, 15 => i=3, rev sort => 12,30,13,16,15 (,26,70,18)
15, 26 => i=4, sort => 12,30,13,16,15,26 (,70,18)
26, 70 => i=5, rev sort => 12,30,13,16,15,70,26 (,18)
70, 18 => i=6, sort => 12,30,13,16,15,70,18,26

Logic:
- The arrangement is local and can be achieved by sorting A[i] and A[i+1] as:
    - i is even => increasing sort
    - i is odd => decreasing sort
"""

from typing import List


class Solution:
    def rearrange_array(self, A: List[int]) -> None:
        for i in range(len(A)):
            A[i:i+2] = sorted(A[i:i+2], reverse=bool(i % 2))

        print(A)

s = Solution()
s.rearrange_array([16,12,30,13,15,26,70,18])