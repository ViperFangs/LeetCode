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