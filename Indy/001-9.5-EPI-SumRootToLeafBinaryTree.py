"""
Input: Binary tree with each node representing a binary digit
Output: Sum of all numbers represented by root -> leaf paths in the Binary Tree
Logic: Visit a node, if it is a leaf node return the integer else return sum of results from left and right children
"""

from BinaryTreeNodeHelper import BinaryTreeNode

class Solution:
    def sum_root_to_leaf(self, tree: BinaryTreeNode) -> int:

        def helper(tree, partial_sum=0):
            if not tree:
                return 0

            # Evaluate the integer from binary value
            partial_sum = partial_sum*2 + tree.data

            # Leaf node: return the value
            if not tree.left and not tree.right:
                return partial_sum

            # traverse down and compute the sum of both child nodes
            return (helper(tree.left, partial_sum) + helper(tree.right, partial_sum))

        return helper(tree)

s = Solution()
T = BinaryTreeNode(1)
T.left = BinaryTreeNode(0)
T.right = BinaryTreeNode(0)
T.left.right = BinaryTreeNode(1)
T.left.right.left = BinaryTreeNode(0)
T.right.left = BinaryTreeNode(1)

print(s.sum_root_to_leaf(T))
