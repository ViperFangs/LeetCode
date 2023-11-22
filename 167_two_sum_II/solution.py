"""
Author: Aarya
Description: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution. You may not use the same element twice.
    Your solution must use only constant extra space.
Time Complexity: O(n), where n is the length of the numbers list
Space Complexity: O(1), the code only utilizes integers
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize left pointer at the start of the list and the right pointer at the end of the list
        l, r = 0, len(numbers) - 1
        # while the left pointer is less than the right pointer
        while l < r:
            # get the current sum of the values at the left and right pointers
            current_sum = numbers[l] + numbers[r]
            """
            if the current sum is greater than the target, then decrement the right pointer
            this is a special property of a sorted array that we can use, because the value at the right pointer is bigger than the value at the left pointer,
                we need to decrement the right pointer so it points to a lower value and the target could be reached
            """
            if current_sum > target:
                r -= 1
            """
            if the current sum is less than the target, then increment the left pointer
            this is done because the value at the left pointer is smaller than the value at the right pointer and as the sum is less than the target
                then we want to increase the left pointer so that we the sum can reach the target value
            """
            elif current_sum < target:
                l += 1
            # if the values at the left and right pointer is equal to the target then return a list with the "index + 1" values (output requirement)
            else:
                return [l + 1, r + 1]