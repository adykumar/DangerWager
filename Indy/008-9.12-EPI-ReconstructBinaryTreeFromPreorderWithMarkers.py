"""
Input: Binary tree with null markers (to show where a child node/leaf is empty)
Output: Reconstructed binary tree
Logic:
Preorder: Node, Left, Right
First node in the sequence has to be the node followed by the left subtree nodes and then the right.
Since the empty nodes/leaves are marked (the sequence essentially is that of a complete tree).
Just solve it recursively!
"""

from BinaryTreeNodeHelper import BinaryTreeNode
from typing import List

class Solution:
    def reconstruct_tree(self, preorder_sequence: List) -> BinaryTreeNode:

        def helper(preorder_iterator):
            subtree_node = next(preorder_iterator)

            # stopping condition
            if subtree_node is None:
                return None

            # recurseively construct left subtree, followed by right and then construct the root node
            left_subtree = helper(preorder_iterator)
            right_subtree = helper(preorder_iterator)
            return BinaryTreeNode(subtree_node, left_subtree, right_subtree)

        return helper(iter(preorder_sequence))

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
         H
        / \
       B   C  
      / \   \
     F  E    D
       /      \
      A        G
              /
             I


T = BinaryTreeNode("H")
T.left = BinaryTreeNode("B")
T.right = BinaryTreeNode("C")
T.left.left = BinaryTreeNode("F")
T.left.right = BinaryTreeNode("E")
T.left.right.left = BinaryTreeNode("A")
T.right.right = BinaryTreeNode("D")
T.right.right.right = BinaryTreeNode("G")
T.right.right.right.left = BinaryTreeNode("I")

Inorder: ["F", "B", "A", "E", "H", "C", "D", "I", "G"]
"""

preorder = ["H", "B", "F", None, None, "E", "A", None, None, None, "C", None,  "D", None, "G", "I", None, None, None]
root: BinaryTreeNode = s.reconstruct_tree(preorder)
print(s.inorder(root))
