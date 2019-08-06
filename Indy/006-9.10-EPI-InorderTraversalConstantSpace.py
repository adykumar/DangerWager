"""
Input: Binary tree where nodes have parent pointers
Output: In-order traversal with constant space (non-recursive)
Logic:
The way to traverse the tree without recursion is to keep track of the parent node for each node
When we return to the parent we need to know whether the subtree just traversed was:
parent's left child => visit parent and traverse right subtree
or
parent's right child => parent's subtree traversal is complete
We do this by tracking the subtree roots and comparing subtree root with parent's left child.
"""

from BinaryTreeNodeHelper import BinaryTreeNodeWithParentPtr
from typing import List

class Solution:
    def inorder_iterative(self, tree: BinaryTreeNodeWithParentPtr) -> List[int]:

        prev, traversal = None, []

        while tree:
            # Traversal path - we came to tree from prev
            if prev is tree.parent:
                # if left subtree exists, go down the subtree
                if tree.left:
                    next = tree.left
                else:
                    # left subtree done, go down right if it's present or move up to parent
                    traversal.append(tree.data)
                    next = tree.right or tree.parent
            # If we came to this node after completing left subtree traversal
            elif tree.left is prev:
                # finished left subtree, add the current subtree root and traverse right subtree if present else move up
                traversal.append(tree.data)
                next = tree.right or tree.parent
            # left and right subtree traversal complete, move up to parent
            else:
                next = tree.parent

            prev, tree = tree, next

        return traversal

s = Solution()
T = BinaryTreeNodeWithParentPtr(314)
T.left = n1 = BinaryTreeNodeWithParentPtr(6)
T.right = n2 = BinaryTreeNodeWithParentPtr(8)
n1.parent = n2.parent = T
T.right.left = n3 = BinaryTreeNodeWithParentPtr(16)
n3.parent = n2
T.left.right = n4 = BinaryTreeNodeWithParentPtr(2)
T.left.left = n5 = BinaryTreeNodeWithParentPtr(42)
n4.parent = n5.parent = n1
T.left.right.left = n6 = BinaryTreeNodeWithParentPtr(26)
n6.parent = n4
T.right.left.right = n7 = BinaryTreeNodeWithParentPtr(21)
n7.parent = n3
"""
        314
        / \
       6   8
      /\   /
    42  2 16
       /   \
      26    21
"""

print(s.inorder_iterative(T))
