"""
986. Interval List Intersections
Medium

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

"""
Time O(a*b)- len of A and B
Space- O(a*b) max
"""

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i=0
        j=0
        res= []
        while i<len(A) and j<len(B):
            a1= A[i][0]
            a2= A[i][1]
            b1= B[j][0]
            b2= B[j][1]
            if b1>=a2:
                if b1==a2: res.append([b1, b1])
                i+=1
                continue
            if a1>=b2:
                if a1==b2: res.append([a1, a1])
                j+=1
                continue
            if b1>=a1 and b1<a2:
                x= max(a1, b1)
                y= min(a2, b2)
                res.append([x,y])
                if b2<=a2: j+=1
                else: i+=1
            elif a1>=b1 and a1<b2:
                x= max(a1, b1)
                y= min(a2, b2)
                res.append([x,y])
                if a2<=b2: i+=1
                else: j+=1
        return res
