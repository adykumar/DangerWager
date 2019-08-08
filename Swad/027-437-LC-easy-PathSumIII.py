"""
437. Path Sum III
Easy

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

"""
Time- O(n)
Space- O(n* 2^n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, root, k, curr, res):
        if root==None: return
        curr.append(0)
        for i in range(len(curr)):
            curr[i]+= root.val
            if curr[i]==k: res[0]+=1

        self.helper(root.left, k, curr[::], res)
        self.helper(root.right, k, curr[::], res)



    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res= [0]
        self.helper(root, sum, [], res)
        return res[0]
        
