""" 
Author: Aarya
Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
Time Complexity: O(n), where n is the length of the nums list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the indices, these variables only require constant space
Logic: The logic for this answer is that we have 2 pointers, L and I. I iterates through the loop.
    If the value at the current I position is not equal to val, then replace the value at the L pointer with the value at the I pointer and increment the L pointer.
    This way the L pointer keeps track of the length of the list that doesn't contain the val variable
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a Left pointer at 0
        L = 0
        # Loop through the nums list
        for i in range(len(nums)):
            # If the current value at I is not equal to val, then replace the value at the L pointer with the value at the I pointer.
            if nums[i] != val:
                nums[L] = nums[i]
                # Increment the L pointer
                L += 1
        # Return the length of the list that doesn't contain the val variable.
        return L