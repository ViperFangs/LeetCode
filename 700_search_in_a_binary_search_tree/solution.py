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

# This class defines a method `searchBST` that recursively searches for a node with a specific value in a binary search tree.
class Recursive:
    """
    This function searches for a specific value in a binary search tree and returns the node
    containing that value if found.
    
    :param root: The `root` parameter in the `searchBST` function represents the root node of a
    binary search tree (BST) from which we want to search for a specific value.

    :param val: The `val` parameter in the `searchBST` function represents the value that we are
    searching for in the binary search tree (BST).

    :return: The function returns either the node with the value equal to the given `val`, or `None` 
    if the node with the value `val` is not found in the binary search tree.
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
# The class contains a method `searchBST` that iteratively searches for a node with a specific value in a binary search tree.
class Iterative:
    """
    This function searches for a specific value in a binary search tree and returns the node
    containing that value if found.
    
    :param root: The `root` parameter in the `searchBST` function represents the root node of a
    binary search tree (BST) from which we want to search for a specific value.

    :param val: The `val` parameter in the `searchBST` function represents the value that we are
    searching for in the binary search tree (BST).

    :return: The function returns either the node with the value equal to the given `val`, or `None` 
    if the node with the value `val` is not found in the binary search tree.
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        
        return None