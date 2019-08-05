"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

"""
Time- O(n)
Space- O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head==None or head.next==None or m==n:
            return head
        h= ListNode(0)
        h.next= head
        a= m-1
        p= h
        while a>0:
            a-=1
            p= p.next
        steps= n-m
        p1= p.next
        p2= p1.next
        while steps:
            steps-=1
            temp= p2.next
            p2.next= p1
            p1= p2
            p2= temp
        p.next.next= temp
        p.next= p1
        return h.next
        
