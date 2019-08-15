"""
124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

"""
Time- O(n)
Space- 1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, root, res):
        if root==None:
            return 0
        left= self.helper(root.left, res)
        right= self.helper(root.right, res)
        temp= root.val + max(left, right)
        res[0]= max(res[0], root.val + left + right, temp, root.val)
        if temp<0: return 0
        return temp

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res= [-float('inf')]
        self.helper(root, res)
        return res[0]
