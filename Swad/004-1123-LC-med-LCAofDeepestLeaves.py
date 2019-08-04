"""
Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.


Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation:
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]


Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
"""

"""
Time- O(n)
SPace- O(n log n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def max_depth(self, root, lev, md):
        if root==None: return
        if root.left==None and root.right==None and lev>md[0]:
            md[0]= lev
        self.max_depth(root.left, lev+1, md)
        self.max_depth(root.right, lev+1, md)

    def helper(self, root, curr, res, cd, md):
        if root==None: return
        temp= curr[::]
        temp.append(root)
        if cd==md:
            res.append(temp)
            return
        self.helper(root.left, temp, res, cd+1, md)
        self.helper(root.right, temp, res, cd+1, md)

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        md= [0]
        self.max_depth(root, 0, md)
        print "maxd:", md[0]
        res= []
        self.helper(root, [], res, 0, md[0])
        anc= root
        for i in range(len(res[0])):
            curr= res[0][i]
            for j in range(len(res)):
                if curr!=res[j][i]:
                    return anc
            anc= curr
        return anc
