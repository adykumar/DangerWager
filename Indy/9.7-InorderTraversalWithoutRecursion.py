"""
Input: Binary tree
Output: Iterative in-order traversal of the tree
Logic: Simulate the function call using a stack. For each node we traverse the left subtree fully and then add it to
result
"""

from BinaryTreeNodeHelper import BinaryTreeNode
from typing import List

class Solution:
    def inorder(self, tree: BinaryTreeNode) -> List[int]:

        # Define output list and the stack to keep track of nodes in progress
        traversal = []
        in_process_stack = [(tree, False)]

        while in_process_stack:
            node, left_subtree_processed = in_process_stack.pop()
            if node:
                # Left subtree processed, now add node to the traversal
                if left_subtree_processed:
                    traversal.append(node.data)
                # Insert Left, node and Right in LIFO order (stack!)
                else:
                    in_process_stack.append((node.right, False))
                    in_process_stack.append((node, True))
                    in_process_stack.append((node.left, False))

        return traversal

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

print(s.inorder(T))
