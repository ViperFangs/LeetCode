""" 
Author: Aarya
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
Time Complexity: O(n) as we only loop through the list once
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store key as the number in the list and the index as the value
        hashmap = {}
        # we can also use for i, n in enumerate(nums) for the loop
        for i in range(len(nums)): 
            # find the difference between the target and the current number
            diff = target - nums[i]
            # if the diff already exists in the set then we return the current index and the index of the diff in the set
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                # if the diff doesn't exist in the set then add it to the set
                hashmap[nums[i]] = i