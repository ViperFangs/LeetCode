"""
Author: Aarya
Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]],
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    the solution set must not contain duplicate triplets.
Time Complexity: O(n^2), as the code uses 2 loops, sorting is an O(nlogn) operation 
Space Complexity: O(1) or O(n), depending on the sorting algorithm used
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list, this is used to deal with duplicates and is similar to two sum II 
        nums.sort()
        # create an empty output list
        output = []
        # the target for this question is 0
        target = 0
        # loop through the list, i is the index and a is the value at that index
        for i, a in enumerate(nums):
            """
            if i is greater than 0, then we want to check if the current value is the same as the previous value,
                if they are the same then we want to move to the next index
            this is done to avoid duplicates in the solution
            """
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # initialize the left pointer as the current index + 1
            l = i + 1
            # initialize the right pointer as the last element in the list
            r = len(nums) - 1
            # while the left pointer is less than the right pointer then enter the loop
            while l < r:
                # find the total sum of the current value, plus the values at the left and right pointers
                total_sum = a + nums[l] + nums[r]
                """ 
                if the total sum is less than the target then increment the left pointer. 
                    This is done as the value at the left pointer is smaller than the value at right pointer. 
                Incrementing the left pointer will increase the total_sum
                """
                if total_sum < target:
                    l += 1
                """ 
                if the total sum is more than the target then decrement the right pointer. 
                    This is done as the value at the left pointer is smaller than the value at right pointer. 
                Decrementing the right pointer will decrease the total_sum
                """
                elif total_sum > target:
                    r -= 1
                """
                    if the total sum is equal to the target then add the 3 values to the output list
                    also increment the left pointer by 1 to check for any other possibilities
                """
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    """
                    After incrementing the left pointer, check if the current value at the left pointer is the same as the previous one
                    this is done to avoid duplicates
                    """
                    while l < r and nums[l] == nums [l - 1]:
                        l += 1
        # return the list that contains a list of values that add up to the target.
        return output