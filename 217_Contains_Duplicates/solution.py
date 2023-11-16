""" 
Author: Aarya
Description: Given an integer array nums, 
    return true if any value appears at least twice in the array,
    and return false if every element is distinct.
Time Complexity: O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        The time complexity for a set is O(1) for the following operations: 
        lookup/insert/delete
        """
        hashset = set()
        for num in nums:
            # if the number already exists in the set then return true
            if num in hashset:
                return True
            # if the number doesn't exist in the set then add it to the set
            else:
                hashset.add(num)
        return False