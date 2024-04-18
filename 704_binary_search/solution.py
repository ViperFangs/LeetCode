""" 
Author: Aarya
Description: Given an array of integers nums which is sorted in ascending order,
  and an integer target, write a function to search target in nums.
    If target exists, then return its index.
    Otherwise, return -1.
  You must write an algorithm with O(log n) runtime complexity.
Time Complexity: O(log(n)), where n is the size of the nums list.
Space Complexity: O(1), we use a few pointers that dont grow with the input.
Logic: The logic here is to split the list in half as it's sorted. 
  If the target value is greater than the mid point, then search the right side of the list.
  If the target value is less than the mid point, then search the left side of the list.
"""

# This Python class implements a binary search algorithm to find the index of a target integer in a
# given list of integers.
class Solution:
    """
    This function performs a binary search on a sorted list of integers to find the index of a
    target value, returning -1 if the target is not found.
    """
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        
        return -1