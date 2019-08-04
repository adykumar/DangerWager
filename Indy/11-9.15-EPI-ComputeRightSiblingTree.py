"""
Input: Binary tree, assumed to be a perfect binary tree. Each node has an extra field (level_next).
Output: Set the level_next field for each node. It should be set to the node directly next to a given node at the
current level.
Logic:
Since the tree is a perfect Binary tree, a node's level next is:
 - If it is a left child, it's the parent's right child.
 - If it is a right child, it's the parent's sibling's left child (which will be set and available to you by the
    time you process this node)
"""

from BinaryTreeNodeHelper import BinaryTreeNodeWithLevelNextPtr
from typing import List

class Solution:
    def construct_right_sibling_tree(self, tree: BinaryTreeNodeWithLevelNextPtr) -> None:

        # use helper function for recursion
        def helper(node):
            while node and node.left:
                # left child's level next will be the right child
                node.left.level_next = node.right

                # if the node is not the last node of the level, set right child's next too
                node.right.level_next = node.level_next and node.level_next.left

                # set node to process next node in the same level
                node = node.level_next

        while tree and tree.left:
            # start at root
            helper(tree)
            # process next level
            tree = tree.left

    def inorder(self, tree: BinaryTreeNodeWithLevelNextPtr) -> List[BinaryTreeNodeWithLevelNextPtr]:

        # Define output list and the stack to keep track of nodes in progress
        traversal = []
        in_process_stack = [(tree, False)]

        while in_process_stack:
            node, left_subtree_processed = in_process_stack.pop()
            if node:
                # Left subtree processed, now add node to the traversal
                if left_subtree_processed:
                    traversal.append(node)
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
      / \  /\
     F  E G  D
       

"""
T = BinaryTreeNodeWithLevelNextPtr("H")
T.left = BinaryTreeNodeWithLevelNextPtr("B")
T.right = BinaryTreeNodeWithLevelNextPtr("C")
T.left.left = BinaryTreeNodeWithLevelNextPtr("F")
T.left.right = BinaryTreeNodeWithLevelNextPtr("E")
T.right.left = BinaryTreeNodeWithLevelNextPtr("G")
T.right.right = BinaryTreeNodeWithLevelNextPtr("D")

s.construct_right_sibling_tree(T)
ll: List[BinaryTreeNodeWithLevelNextPtr] = s.inorder(T)
for l in ll:
    if l.level_next:
        print("Level next for " + l.data + " is: " + l.level_next.data)
    else:
        print("No level next for: " + l.data)
