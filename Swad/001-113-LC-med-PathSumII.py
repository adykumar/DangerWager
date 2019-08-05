
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

"""
Time- O(n)
Space- ???
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, root, s, curr, res):
        temp= curr[::]
        if root==None: return
        temp.append(root.val)
        #print temp, sum(temp)
        if root.left==None and root.right==None and sum(temp)==s:
            res.append(temp)
            return
        self.helper(root.left, s, temp, res)
        self.helper(root.right, s, temp, res)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res= []
        curr= []
        self.helper(root, sum, curr, res)
        return res
