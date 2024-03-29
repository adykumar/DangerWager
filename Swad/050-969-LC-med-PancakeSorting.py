"""
969. Pancake Sorting
Medium

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""

"""
Time- O(n^2) worst case, as each out of place max requires 2 flips
Space- O(1) : in place
"""

class Solution(object):

    def rev(self, A, j, res):
        if j==0: return
        res.append(j+1)
        i=0
        while i<j:
            A[i], A[j]= A[j], A[i]
            i+=1
            j-=1

    def idx_max(self, A, l):
        Max= A[0]
        maxpos= 0
        i=0
        for x in A[1:l+1]:
            i+=1
            if x>Max:
                Max= x
                maxpos= i
        return maxpos

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l= len(A)-1
        res= []
        while l>0:
            idx= self.idx_max(A, l)
            self.rev(A, idx, res)
            self.rev(A, l, res)
            l-=1
        return res
