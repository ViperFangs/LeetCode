""" 
Author: Aarya
Description: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Time Complexity: O(V + E), where V represents the number of vertices and E represents the number of edges in the graph
Space Complexity: O(V), where V represents the number of vertices in the graph. The algorithm also utilizes a list to keep track of the nodes on each level
Logic: The logic here is to use BFS to go through the graph (a.k.a Level order traversal)
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create an output list[list[]] that will store all the nodes on a level
        output = []
        # Create a new queue
        queue = deque()
        #  If root exists then add it to the queue
        if root:
            queue.append(root)
        # While there are still level's remaining
        while queue:
            # Create a list to hold all the nodes on a level
            level_nodes = []
            # Go through each level
            for i in range(len(queue)):
                # Pop the first item that went into the queue
                temp = queue.popleft()
                # Add the val of the current node to the list of level_nodes
                level_nodes.append(temp.val)
                # If this node has any left or right nodes then add it to the queue
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # The algorithm has traversed through a level, add the value of the nodes to the 2D output list 
            output.append(level_nodes)
        # return the final output
        return output