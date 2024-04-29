""" 
Author: Aarya
Description: Given the root of a binary search tree, and an integer k, 
  return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Time Complexity: O(n), Both the solutions takes n time to execute, 
  as it has to go through all the nodes in the tree
Space Complexity: O(log(n)) for iterative(balanced), O(n) for iterative(skewed tree), O(n) for Recursive
  Iterative: Uses a stack to keep track of the nodes. Will grow with the size of the input.
  Recursive: The height of the recursive tree will be equal to the log(n). 
  However we use a result list which will grow with the input making the space complexity as O(n).
Logic: 
  Iterative: Keep going to the left using a temp pointer, once at the end pop the stack, reduce value of k,
    add the val to result and change temp node to point to the right subtree.
    Once k reaches 0, return the value of the current_node as that will be the Kth smallest element in the tree.  
  Recursive: Recursively call the same method on the left subtree, then add the current node to the result,
    then recursively call the method on the right subtree.
    At the end return result[k - 1] as the list will be sorted due to inorder traversal.
"""

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# This class defines a method to find the kth smallest element in a binary search tree using an iterative approach.
class Iterative:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      current = root
      stack = []

      while current or stack:
          while current:
              stack.append(current)
              current = current.left
          current = stack.pop()
          k -= 1

          if k == 0:
              return current.val

          current = current.right
    
# This class defines a method to find the kth smallest element in a binary search tree using recursive depth-first search.
class Recursive:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      result = []

      def dfs(node):
          if not node:
              return
          
          dfs(node.left)
          result.append(node.val)
          dfs(node.right)

      dfs(root)
      return result[k - 1]