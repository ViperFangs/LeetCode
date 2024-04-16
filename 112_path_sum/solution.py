# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        return self.canReachLeaf(root, path, targetSum)
        
    def canReachLeaf(self, root: TreeNode, path: List[int], target: int) -> bool:
        if not root:
            return False

        path.append(root.val)

        if not root.left and not root.right and sum(path) == target:
            return True
        if self.canReachLeaf(root.left, path, target):
            return True
        if self.canReachLeaf(root.right, path, target):
            return True
        
        path.pop()
        return False