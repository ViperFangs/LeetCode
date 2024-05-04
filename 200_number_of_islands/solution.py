"""
Author: Aarya
Description: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
  You may assume all four edges of the grid are all surrounded by water.
Time Complexity: O(m * n), where M is the number of rows and N is the number of columns in the grid.
  This complexity arises because each cell in the grid is visited exactly once. 
Space Complexity: O(m * n), in the worst case, the space complexity reaches O(M * N), which is determined by the size of the call stack.
  This worst-case scenario occurs when the grid is filled entirely with '1's, 
  leading to the maximum depth of the recursive call stack equaling the number of elements in the grid.
"""

# This class implements a solution to count the number of islands in a grid using depth-first search.
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    
    visited = set()
    islands = 0
    # The `directions` list contains the possible movements that can be made from a cell in the
    # grid. Each element in the list represents a direction to move in the grid.
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(r, c):
      """
      The function uses depth-first search to count the number of islands in a grid represented by
      "1"s and "0"s.
      """
      if ((r == ROWS or c == COLS) or ((r, c) in visited) or (min(r, c) < 0) or (grid[r][c] == "0")):
        return

      visited.add((r, c))

      for dr, dc in directions:
        dfs(r + dr, c + dc)
        
    for i in range(ROWS):
      for j in range(COLS):
        if (grid[i][j] == "1") and ((i, j) not in visited):
          islands += 1
          dfs(i, j)

    return islands