""" 
Author: Aarya
Description: Given an integer array nums and an integer k, 
    return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Time Complexity: O(n), where n is the size of the nums list
Space Complexity: O(k), The algorithm uses a hashset that could be as large as k
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize the left pointer at the start of the list
        l = 0
        # Initialize a hashset to store values
        window = set()
        # loop through the list using the right pointer, the right pointer starts at 0
        for r in range(len(nums)):
            # if the size of the window is greater than k then we want to reduce the size
            if r - l > k:
                # remove the element at the left pointer from the hashset
                window.remove(nums[l])
                # increment the left pointer so that the length of the window is less than k
                l += 1
            # if the value at the right pointer is not in the hashset then add it to the hashset
            if nums[r] not in window:
                window.add(nums[r])
            # if there are duplicates then return True as we always maintain the size of the window to be less than k
            else:
                # return True if the value at the right pointer exists in the hashset.
                return True
        # return False if the code hasn't returned True by now.
        return False