""" 
Author: Aarya
Description: Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Time Complexity: O(V + E), where V represents the number of vertices and E represents the number of edges in the graph
Space Complexity: O(V), where V represents the number of vertices in the graph. The algorithm also utilizes a list to keep track of the nodes on each level
Logic: The logic here is to use BFS to go through the graph (a.k.a Level order traversal).
    At the end of each level, add the value of the last node visited as that will be the right node. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Import Double Ended Queue from collections as its required for the BFS algorithm
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Create an output list to hold all the right side nodes
        output = []
        # Create a new queue
        queue = deque()
        # If root exists then add it to the queue
        if root:
            queue.append(root)
        # Utilize BFS to go through the graph
        while queue:
            # This is the start of each level, the left most node should be at the start of the queue
            # Visit the nodes at the current level
            for i in range(len(queue)):
                # Pop the first element in the queue
                temp = queue.popleft()
                # If the current node as neighbors then add them to the queue
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # This is the end of each level, the last visited node is the right most node of the current level
            # Add the last visited node to the output as that is the right most node of the current level
            output.append(temp.val)
        # Return output. Output contains all the right sided nodes in the tree
        return output