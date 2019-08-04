"""
Input: Binary Tree
Output: Exterior of the Binary tree. In O(N) time
Logic: The exterior of a tree can be broken down into:
1. Left (Top -> Bottom left edge)
2. Leaves (L->R)
3. Right (Bottom -> Top right edge)
"""

from BinaryTreeNodeHelper import BinaryTreeNode
from typing import List

class Solution:
    def compute_exterior(self, tree: BinaryTreeNode) -> List[BinaryTreeNode]:

        # compute left boundary
        def compute_left_boundary(subtree):
            # leaf reached, append the node to result
            if not subtree or (not subtree.left or not subtree.right):
                return
            exterior.append(subtree)

            # recurse down left if left subtree exists else go down right
            if subtree.left:
                compute_left_boundary(subtree.left)
            else:
                compute_left_boundary(subtree.right)

        # compute right boundary
        def compute_right_boundary(subtree):
            if not subtree or (not subtree.left and not subtree.right):
                return

            # Do not append after this, since we want the order reversed leaf -> root, we append after recursing down
            # recurse down right if right subtree exists else recurse down left
            if subtree.right:
                compute_right_boundary(subtree.right)
            else:
                compute_right_boundary(subtree.left)
            exterior.append(subtree)

        # compute leaves L-> R
        def compute_leaves(subtree):
            if not subtree:
                return

            # leaf node, so append
            if not subtree.left and not subtree.right:
                exterior.append(subtree)

            compute_leaves(subtree.left)
            compute_leaves(subtree.right)

        # start point - edge case
        if not tree:
            return []

        # combine it
        exterior = [tree]
        compute_left_boundary(tree.left)
        compute_leaves(tree.left)
        compute_leaves(tree.right)
        compute_right_boundary(tree.right)
        return exterior

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

ll = s.compute_exterior(T)
for l in ll:
    print(l.data)

