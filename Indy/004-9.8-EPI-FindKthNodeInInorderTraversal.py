"""
Given: Binary tree and an integer K. Each node contains the # of nodes in the subtree rooted at this node.
Output: Kth node in the in-order traversal of the tree
Logic: To efficiently compute the kth node, see if k is less than the # nodes in the subtree rooted here. Use this to
direct your search and prune search space
"""

from BinaryTreeNodeHelper import BinaryTreeNodeWithSubtreeSize
from typing import Optional

class Solution:
    def kth_node_in_binary_tree(self, tree: BinaryTreeNodeWithSubtreeSize, k: int) -> \
            Optional[BinaryTreeNodeWithSubtreeSize]:

        while tree:
            leftSubtree_size = tree.left.size if tree.left else 0

            # if left-subtree-size+1 < k i.e. node is in the right subtree
            if leftSubtree_size + 1 < k:
                k -= leftSubtree_size + 1
                tree = tree.right
            # if the root is the kth node i.e. left-subtree-size+1 == k
            elif leftSubtree_size == k-1:
                return tree
            # if it is present in the left subtree
            else:
                tree = tree.left

        return None

s = Solution()
"""
         4
         /\
        6  18
        \  /
        2  2
        /
        2

[6, 2, 2, 4, 2, 18]
"""

T = BinaryTreeNodeWithSubtreeSize(4, None, None, 6)
n1 = BinaryTreeNodeWithSubtreeSize(6, None, None, 3)
n2 = BinaryTreeNodeWithSubtreeSize(18, None, None, 2)
n3 = BinaryTreeNodeWithSubtreeSize(2, None, None, 2)
n4 = BinaryTreeNodeWithSubtreeSize(2, None, None, 1)
n5 = BinaryTreeNodeWithSubtreeSize(2, None, None, 1)
T.left = n1
T.right = n2
n1.right = n3
n2.left = n4
n3.left = n5

print(s.kth_node_in_binary_tree(T, 1).data)
print(s.kth_node_in_binary_tree(T, 2).data)
print(s.kth_node_in_binary_tree(T, 3).data)
print(s.kth_node_in_binary_tree(T, 4).data)
print(s.kth_node_in_binary_tree(T, 5).data)
print(s.kth_node_in_binary_tree(T, 6).data)
