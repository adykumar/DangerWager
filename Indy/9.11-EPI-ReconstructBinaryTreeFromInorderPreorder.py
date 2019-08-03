"""
Input: Binary tree traversal - In-order and Pre-order
Output: Reconstructed binary tree
Logic:
Pre-order traversal tells us the root and splits the in-order sequence into right and left subtrees
We use the left subtree in-order sequence to figure out the left subtree preorder sequence from the tree's preorder
sequence"""

from BinaryTreeNodeHelper import BinaryTreeNode
from typing import List

class Solution:
    def reconstruct_tree(self, preorder: List, inorder: List) -> BinaryTreeNode:

        # node to index mapping for inorder sequence
        inorder_node_idx_map = {data: i for i, data in enumerate(inorder)}

        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            # stopping condition - if the start and end cross over
            if preorder_end <= preorder_start or inorder_end <= inorder_start:
                return None

            # find the index of root which is 1st preorder element in the inorder sequence
            inorder_root_idx = inorder_node_idx_map[preorder[preorder_start]]

            # find size of the left subtree
            left_subtree_size = inorder_root_idx - inorder_start

            # create root node and recursively build the subtrees
            return BinaryTreeNode(
                preorder[preorder_start],  # data
                helper(preorder_start+1, preorder_start+1+left_subtree_size, inorder_start, inorder_root_idx),  # left
                helper(preorder_start+1+left_subtree_size, preorder_end, inorder_root_idx+1, inorder_end)  # right
            )
        return helper(0, len(preorder), 0, len(inorder))

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
"""

inorder = ["F", "B", "A", "E", "H", "C", "D", "I", "G"]
preorder = ["H", "B", "F", "E", "A", "C", "D", "G", "I"]
root: BinaryTreeNode = s.reconstruct_tree(preorder, inorder)
print(s.inorder(root))
