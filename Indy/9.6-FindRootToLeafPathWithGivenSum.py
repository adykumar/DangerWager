"""
Input: Binary tree with each node labeled with an integer and a given integer
Output: Check if a root -> leaf path exists whose path sum == given integer
Logic: Traverse the tree and keep track of remaining sum. If we find a leaf with integer = remaining sum, return true
"""

from BinaryTreeNodeHelper import BinaryTreeNode

class Solution:
    def has_path_sum(self, tree: BinaryTreeNode, remaining_sum: int) -> bool:
        if not tree:
            return False

        # Leaf node, check if remaining sum == remaining sum
        if not tree.left and not tree.right:
            return remaining_sum == tree.data

        return(self.has_path_sum(tree.left, remaining_sum-tree.data) or self.has_path_sum(tree.right,
                                                                                          remaining_sum-tree.data))

s = Solution()

"""
         4
         /\
        6  18
        \  /
        2  2
        /
        2
"""

T = BinaryTreeNode(4)
T.left = BinaryTreeNode(6)
T.right = BinaryTreeNode(18)
T.left.right = BinaryTreeNode(2)
T.left.right.left = BinaryTreeNode(2)
T.right.left = BinaryTreeNode(2)

print(s.has_path_sum(T, 24))
print(s.has_path_sum(T, 2))
print(s.has_path_sum(T, 200))