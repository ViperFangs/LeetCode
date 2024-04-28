""" 
Author: Aarya
Description: Given the root of a binary tree, return the inorder traversal of its nodes' values.
Time Complexity: O(n), Both the solutions takes n time to execute, 
  as it has to go through all the nodes in the tree
Space Complexity: O(n) for both solutions
  Both the solutions use a list to keep track of all the node values,
    the list will grow with the size of the input
Logic: 
  Iterative: Keep going to the left using a temp pointer, once at the end pop the stack,
    add the val to result and change temp node to point to the right subtree.  
  Recursive: Recursively call the same method on the left subtree, then add the current node to the result,
    then recursively call the method on the right subtree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This class defines a method `inorderTraversal` that performs a iterative inorder
# traversal on a binary tree and returns the result as a list of integers.
class Iterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            result.append(current_node.val)
            current_node = current_node.right
        
        return result

# This class defines a method `inorderTraversal` that performs a recursive inorder
# traversal on a binary tree and returns the result as a list of integers.
class Recursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root, [])
        
    def inorder(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return
        
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)

        return result