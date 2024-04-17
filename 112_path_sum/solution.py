"""
Author: Aarya
Description: Given the root of a binary tree and an integer targetSum, 
    return true if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals targetSum.
    Note: A leaf is a node with no children.
Time Complexity: O(n), where n is the amount of variables in the tree. 
    Backtracking solutions generally have the time complexity of O(n)
    This is because in the worst case, the solution will go through all the variables.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
      def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Return False if the current node is None
        if not root:
            return False
        # If the current node is a Leaf Node and if the targetSum is reached then return True
        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        # Recursively check the left node
        if self.hasPathSum(root.left, targetSum - root.val):
            return True
        # Recursively check the right node
        if self.hasPathSum(root.right, targetSum - root.val):
            return True
        # If no solution was found then return False
        return False