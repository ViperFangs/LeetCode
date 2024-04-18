""" 
Author: Aarya
Description: You are given the root node of a binary search tree (BST) and a value to insert into the tree.
  Return the root node of the BST after the insertion.
  It is guaranteed that the new value does not exist in the original BST.
  Notice that there may exist multiple valid ways for the insertion,
  as long as the tree remains a BST after insertion. You can return any of them.
Time Complexity: O(log(n)), where log(n) is the height of the tree.
Space Complexity: O(1), we only create a new node and the algorithm doesn't use more space based on the input.
Logic: The logic here is to recursively add the val to the correct spot by checking if the value is greater or lower than the current node.
  Once the current node becomes null, a new node is created which is then attached to the parent.
"""

# Definition for a binary tree node.
# The class TreeNode defines a node structure for a binary tree with attributes for value, left child, and right child.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This Python class defines a solution for inserting a node with a given value into a binary search tree.
class Solution:
    """
    This function inserts a new node with a given value into a binary search tree while maintaining
    the binary search tree property.
    
    :param root: The `root` parameter represents the root node of a binary search tree (BST) where
    you want to insert a new node with the value `val`. If the `root` is `None`, it means the tree
    is empty, and the new node with the value `val` will become the root.

    :param val: The `val` parameter in the `insertIntoBST` function represents the value that you
    want to insert into the Binary Search Tree (BST). The function recursively inserts this value
    into the BST based on the comparison with the values of nodes in the tree.
    
    :return: the updated root of the binary search tree after inserting the new node with the value
    'val'.
    """ 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root