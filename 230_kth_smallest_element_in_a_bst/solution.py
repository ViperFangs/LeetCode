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