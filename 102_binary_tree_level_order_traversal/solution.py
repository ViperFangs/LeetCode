# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            level_nodes = []
            for i in range(len(queue)):
                temp = queue.popleft()
                level_nodes.append(temp.val)
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            output.append(level_nodes)
        
        return output