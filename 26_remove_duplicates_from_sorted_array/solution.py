""" 
Author: Aarya
Description: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
Time Complexity: O(n), where n is the length of the nums list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the indices, these variables only require constant space
Logic: The logic for this answer is that we have 2 pointers, L and R. Left keeps track of the length of the nums list that has non-duplicate elements.
    for e.g. for [1,2,3,4], L will be equal to 4
    The R pointer is used to find if the character at the current index of R and the one behind it are the same or not,
    if same, then they are duplicates
    if not the same, then a new number is present at the R location, replace the value at the left pointer with the value at the right pointer. 
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the L pointer to be 1, the first element (0) can not be a duplicate
        L = 1
        # Use the R pointer to traverse the nums list starting from index 1
        for R in range(1, len(nums)):
            # If the value at R and the one behind it aren't the same then a new non duplicate value is found
            if nums[R] != nums[R - 1]:
                # Replace the value at the L pointer with the value at the right pointer
                nums[L] = nums[R]
                # Increment L by 1
                L += 1
        # Return L as it contains the length of the list that has no duplicates
        return L