"""
147. Insertion Sort List
Medium

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


"""
Time- Worst O(n^2)
Space- 0
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        h= ListNode(-float('inf'))
        h.next= head
        p= h
        while True:
            t= p.next
            p.next= t.next
            trav= h
            while trav.next and trav.next.val<t.val:
                trav= trav.next
            x= trav.next
            trav.next= t
            t.next= x
            if p.next==None or p.next.next==None:
                break
            if p.val<p.next.val:
                p= p.next
        return h.next
