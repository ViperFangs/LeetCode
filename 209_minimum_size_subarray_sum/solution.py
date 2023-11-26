""" 
Author: Aarya
Description: Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
    whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Time Complexity: O(n), where n is the size of the nums list
Space Complexity: O(1), The algorithm uses a few variables that don't grow with the input
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Initialize output as the length of the nums + 1, as that can never be the length of a subarray for the nums list
            This information will be used at the end to return the output or 0
        """
        output = len(nums) + 1
        # Initialize a left pointer at the start of the nums list
        l = 0
        # Initialize current_sum as 0
        current_sum = 0
        # loop through the nums list using a right pointer
        for r in range(len(nums)):
            # Add the current value at the right pointer to the current sum
            current_sum += nums[r]
            """
            While the current_sum is greater than or equal to the target value, then:
                Update the output value to be smaller of current length of the window or the output itself
                    (r - l + 1) is used to find the length of the current window
                Subtract the value at the left pointer from the current sum
                Increment the left pointer
            """
            while current_sum >= target:
                output = min(output, r - l + 1)
                current_sum -= nums[l]
                l += 1
        # Return 0 if the output is the same length as when it was initialized, else return the value of the output
        return 0 if output == len(nums) + 1 else output