"""
Input: Binary Tree
Output: List of leaves of the binary tree ordered from L-> R
Logic:
We traverse the tree in order (L-Root-R), only when we encounter a leaf we add it to the final result.
Single pass, O(N)
"""

from BinaryTreeNodeHelper import BinaryTreeNode
from typing import List

class Solution:
    def create_list_from_leaves(self, tree: BinaryTreeNode) -> List[BinaryTreeNode]:
        # stopping condition
        if not tree:
            return []

        # Leaf node=> add to resultset
        if not tree.left and not tree.right:
            return [tree]

        # else recurse down left and then right and concatenate them
        return self.create_list_from_leaves(tree.left) + self.create_list_from_leaves(tree.right)


s = Solution()

"""
         H
        / \
       B   C  
      / \   \
     F  E    D
       /      \
      A        G
              /
             I

"""
T = BinaryTreeNode("H")
T.left = BinaryTreeNode("B")
T.right = BinaryTreeNode("C")
T.left.left = BinaryTreeNode("F")
T.left.right = BinaryTreeNode("E")
T.left.right.left = BinaryTreeNode("A")
T.right.right = BinaryTreeNode("D")
T.right.right.right = BinaryTreeNode("G")
T.right.right.right.left = BinaryTreeNode("I")

ll = s.create_list_from_leaves(T)
for l in ll:
    print(l.data)
