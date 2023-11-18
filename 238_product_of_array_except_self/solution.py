""" 
Author: Aarya
Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
Time Complexity: O(n) where n is the size of nums
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize a result list of the same size as that of nums
        result = [1] * len(nums)
        # initialize prefix and postfix variable as one, they will be used to populate the result list
        prefix = 1
        postfix = 1
        # loop through the nums/result list(same size)
        for i in range(len(nums)):
            """
            Assign the current index as the prefix value in the result list
            the prefix of every element up until nums[i - 1] will be stored in result[i]
            """ 
            result[i] = prefix
            """
            multiply the prefix value with the value stored in the current index of nums
            this value will be used in the next iteration
            """
            prefix *= nums[i]
        # loop through the lists in backwards order to calculate the postfix value
        for i in range(len(nums) - 1, -1, -1):
            """
            mutiply the current index of the result list with the postfix to get the product of current index except self
            this is possible because the prefix of every element up until nums[i - 1] is stored in result[i], 
                that way when we multiple the postfix with the value at result[i] we get the product of that element in the list except self
            """
            result[i] *= postfix
            # multiply the postfix with the element at nums[i]
            postfix *= nums[i]
        # At this point, the result will be the Product of Array Except Self
        return result