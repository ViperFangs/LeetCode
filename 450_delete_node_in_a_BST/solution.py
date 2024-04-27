""" 
Author: Aarya
Description: Given a root node reference of a BST and a key, delete the node with the given key in the BST.
  Return the root node reference (possibly updated) of the BST.
  Basically, the deletion can be divided into two stages:
    Search for a node to remove.
    If the node is found, delete the node.
Time Complexity: O(log(n)), The algorithm eliminates half the possible values after each recursive call.
  Deleting a node from a BST is a log(n) operation.
Space Complexity: O(log(n)), The memory complexity of a recursive function is the height of the call stack. 
Logic: The logic here is that we first find the node with the specified value.
  If that node has no children then we can safely delete the node
  If the node has one children then we can replace the node that is going to be deleted with the child.
  If the node has 2 children, then we want to find the minValue node present in the right subtree.
    Replace the current node value with the min node.
    Then we call the function one more time to delete the minValue node.
  We use the right subtree because the lowest value in right subtree will replace the current node and still maintain the BST property.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# This Python class provides a method to delete a node with a specific key from a binary search tree.
class Solution:
    """
    This function deletes a node with a specific key from a binary search tree while maintaining the
    binary search tree property.
    
    :param root: The `root` parameter is a reference to the root node of a binary search tree (BST).
    
    :param key: The `key` parameter in the `deleteNode` function represents the value that we want
    to delete from the binary search tree. The function recursively searches for the node with the
    given key value and removes it from the tree while maintaining the binary search tree properties

    :return: the updated root node of the binary search tree after deleting the node with the specified key.
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minValue = self.findMinValue(root.right)
                root.val = minValue
                root.right = self.deleteNode(root.right, minValue)
        return root
    
    """
    The function finds the minimum value in a binary tree starting from the given root node.
    
    :param root: The `root` parameter in the `findMinValue` function is referring to the root node 
    of a binary search tree (BST). 

    :return: The method returns the value of the leftmost node, which is the minimum value in the binary search tree.
    """
    def findMinValue(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp.val