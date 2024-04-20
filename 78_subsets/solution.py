""" 
Author: Aarya
Description: Given an integer array nums of unique elements, return all possible subsets(the power set).
  The solution set must not contain duplicate subsets. Return the solution in any order.
Time Complexity: O(n), This approach uses a backtracking approach which will go through each index.
Space Complexity: O(n), This approach uses a list to store all the subsets. This list will grow with the input.
Logic: The logic here is to add elements to the subset list,
  and then when the index becomes greater than the length of the list,
  we add the current subset to result and backtrack to find other subsets.
  This is a backtracking algorithm and it makes 2 decision at each node.

  Eg: If the nums list is [[1, 2]]: The algorithm will first add [1, 2] to the result,
    then it will pop 2, go out of bounds and add [1] to the result, 
    then it will pop 1, go to the first index, go out of bounds and add [2] to the result,
    then it will pop 2, go out of bounds and add [] to the result.
"""

# The `Solution` class in Python defines a method `subsets` that generates all possible subsets of a
# given list of integers using depth-first search.
class Solution:
    """
    The function generates all possible subsets of a given list of integers using depth-first search
    (DFS) algorithm.
    
    :param nums: The `nums` parameter in the given code represents a list of integers for which we
    want to find all possible subsets.

    :return: A list of all possible subsets of the input list of integers is being returned.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Make a decision to add the current index to the subset list
            subset.append(nums[i])
            dfs(i + 1)

            # Make a decision to NOT add the current index to the subset list
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return result