# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# This Python class provides a method to delete a node with a specific key from a binary search tree.
class Solution:
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
            
    def findMinValue(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp.val