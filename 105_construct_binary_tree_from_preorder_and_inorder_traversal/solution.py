"""
Author: Aarya
Description: Given two integer arrays preorder and inorder
  where preorder is the preorder traversal of a binary tree 
  and inorder is the inorder traversal of the same tree,
  construct and return the binary tree.
Time Complexity: O(n), where n is the amount of variables in the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution assumes that there are no duplicates in the tree.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If either of the traversal list is empty then return from this method
        if not preorder or not inorder:
            return None
        # The first value of the preorder list is always the root value (by definition)
        root = TreeNode(preorder[0])
        """
        Find the mid point index in the inorder list, the mid point is the value of the root
        After closely examining the inorder list, we can notice that the mid point splits the list in 2 halves.
          The first half consists of all the values that are on the left side of the tree
          The second half consists of all the values that are on the right side of the tree
        """
        mid = inorder.index(preorder[0])
        # Recursively call the buildTree method to fill the left half of the tree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # Recursively call the buildTree method to fill the right half of the tree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root