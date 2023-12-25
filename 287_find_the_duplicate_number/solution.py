""" 
Author: Aarya
Description: Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
Time Complexity: O(n), where n is the length of the nums list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the indices, these variables only require constant space
Logic: The logic for this answer is that its a linked list cycle problem, we have to traverse through the list using the list entries as index numbers
    For e.g. for the list [1,3,4,2,2], the first traversal will go to nums[1], which leads to nums[3], which then leads to nums[2] and so on.
    The important part here is because there is a duplicate present, then there will be a cycle present when using the Floyd's algorithm. 
    We can use slow and fast pointers to solve this problem.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize 3 variables that will iterate over the nums list
        cycle_start, fast, slow = 0, 0, 0
        # This loop is bound to stop when a duplicate has been found. Floyd's algorithm guarantees O(n) runtime.
        while True:
            # Move the slow pointer by 1
            slow = nums[slow]
            # Move the fast pointer by 2
            fast = nums[nums[fast]]
            # When both fast and slow are same then that confirms a cycle exist
            if slow == fast:
                # Use the floyd's algorithm to determine the start of the cycle
                # The distance from the slow pointer to the start of the cycle is the same as the distance from the head of the list to the start of the cycle
                while cycle_start != slow:
                    slow = nums[slow]
                    cycle_start = nums[cycle_start]
                # return the start of the cycle when slow and cycle_start are the same
                return cycle_start