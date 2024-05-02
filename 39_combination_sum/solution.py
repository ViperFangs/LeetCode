# This class provides a method that finds all unique combinations of candidates
# that sum up to a target value using backtracking.
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # The list res will track all the combinations that can reach the target value
    res = []
    # The function `dfs` recursively explores all possible combinations of elements from a list
    #`candidates` to reach a target sum `target`.
    def dfs(i, cur, total):
      # Base case when total reaches target
      if total == target:
          res.append(cur.copy())
          return
      # Base case when total becomes greater than target or index goes out of bounds
      if i >= len(candidates) or total > target:
          return

      # Decision to add the current index to the cur list
      cur.append(candidates[i])
      dfs(i, cur, total + candidates[i])
      # Decision to NOT add the current index to the cur list
      cur.pop()
      dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res