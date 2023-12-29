# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                temp = queue.popleft()
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            output.append(temp.val)

        return output