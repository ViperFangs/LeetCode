""" 
Author: Aarya
Description: Given an integer array nums of length n, 
    you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    Return the array ans.
Time Complexity: O(n), where n is the length of the nums list.
Space Complexity: O(1), the algorithm uses no extra variables
Logic: The logic here is to loop through each variable and append it to the end.
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Loop through the list and add each variable to the end.
        for i in range(len(nums)):
            nums.append(nums[i])
        
        return nums