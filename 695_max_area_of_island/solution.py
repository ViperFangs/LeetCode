"""
Author: Aarya
Description: You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
  You may assume all four edges of the grid are surrounded by water.
  The area of an island is the number of cells with a value 1 in the island.
  Return the maximum area of an island in grid. If there is no island, return 0.
Time Complexity: O(m * n), where M is the number of rows and N is the number of columns in the grid.
  This complexity arises because each cell in the grid is visited exactly once. 
Space Complexity: O(m * n), in the worst case, the space complexity reaches O(M * N), which is determined by the size of the call stack.
  This worst-case scenario occurs when the grid is filled entirely with '1's, 
  leading to the maximum depth of the recursive call stack equaling the number of elements in the grid.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      """
      The function `maxAreaOfIsland` in Python calculates the maximum area of an island in a grid
      """
      ROWS, COLS = len(grid), len(grid[0])
      # Use a set to track which rows and cols have been visited
      visited = set()
      max_area = 0
      # Define the 4 different directions that a node can move to
      directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

      def dfs(r, c, islands):
        """
        The function `dfs` performs depth-first search on a grid to find connected islands starting
        from a given position (r, c).
        """
        if min(r, c) < 0 or r == ROWS or c == COLS or not grid[r][c] or (r, c) in visited:
            return
        
        visited.add((r, c))
        islands.append([r, c])
        for dr, dc in directions:
          dfs(r + dr, c + dc, islands)
    
      for r in range(ROWS):
        for c in range(COLS):
          if grid[r][c] and (r, c) not in visited:
            islands = []
            area = dfs(r, c, islands)
            max_area = max(len(islands), max_area)

      return max_area