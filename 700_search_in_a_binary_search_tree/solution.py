""" 
Author: Aarya
Description: You are given the root of a binary search tree (BST) and an integer val.
  Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
  If such a node does not exist, return null.
Time Complexity: O(log(n)), Both the solutions take log(n) time to execute as BST is sorted 
  and the algorithm gets rid of half the input on each execution.
Space Complexity: O(1) for Iterative; O(log(n)) for Recursive
  The iterative solution only uses a few pointers that dont grow with the input.
  For a recursive function, the space time complexity is equal to the depth of the call tree.
Logic: 
  Iterative: Go to the right or left subtree depending on the root's value and target value.
  Recursive: Recursively call the same method on the right or left subtree depending on the root's value and target value.
"""

class Recursive:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
class Iterative:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        
        return None