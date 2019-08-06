"""
Input: A binary tree where each node stores it's parent. A node.
Output: Inorder successor of the given node.
Logic: The trick to prune the search space is to check
If the given node has a right subtree.
    If yes, the successor is in that subtree - the first node visited there.
    Else it does not have a right subtree, then
        If the node is it's parent left child, the parent is the successor
        Else if node is the parent's right child, we iteratively follow the parents until we move up from a left child
        In case we reach the root without ever moving up from a left child => rightmost leaf. Answer is None in that
        case.

"""

from BinaryTreeNodeHelper import BinaryTreeNodeWithParentPtr
from typing import Optional

class Solution:
    def find_successor(self, node: BinaryTreeNodeWithParentPtr) -> Optional[BinaryTreeNodeWithParentPtr]:

        # check for right subtree. If present, return leftmost leaf/node
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # Find the closest parent whose left subtree contains the node
        while node.parent and node.parent.right is node:
            node = node.parent

        return node.parent

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

print(s.find_successor(n6).data)
print(s.find_successor(n7).data)
print(s.find_successor(n4).data)
